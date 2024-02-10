import React, { useState, useEffect } from 'react'
import { AE_AMOUNT_FORMATS } from '@aeternity/aepp-sdk'
import useAeternitySDK from './components/useAeternitySDK.ts'
import BackGroundImage from './assets/BackGround.jpg'
import ChatBot from './ChatBot.jsx'
import './assets/Connect.css'
import image1 from './assets/image1.jpeg';
import image2 from './assets/image2.jpeg';
//networkId
const Connect = () => {
    const { aeSdk, connectToWallet, address, getBalance } = useAeternitySDK();
    const [isLoading, setIsLoading] = useState(false);
    const [balance, setBalance] = useState(null);
    const [spendTo, setSpendTo] = useState('');
    const [spendAmount, setSpendAmount] = useState('');
    const [thankYouVisible, setThankYouVisible] = useState(false);
    const [noAmount, setnoAmount] = useState(false);
    // const [spendPayload, setSpendPayload] = useState('Default Payload');
    // const [spendPromise, setSpendPromise] = useState(null);
    const [showChatbot, setShowChatbot] = useState(false);

    const ngoImages = [
        { src: image1, description: 'Image 1 Description' },
        { src: image2, description: 'Image 2 Description' },
    ];
    let aci = [
        {
            "contract": {
                "functions": [
                    {
                        "arguments": [],
                        "name": "init",
                        "payable": false,
                        "returns": "CharityTransfer.state",
                        "stateful": false
                    },
                    {
                        "arguments": [],
                        "name": "sendMoney",
                        "payable": true,
                        "returns": {
                            "tuple": []
                        },
                        "stateful": true
                    },
                    {
                        "arguments": [],
                        "name": "getContractDetails",
                        "payable": false,
                        "returns": "CharityTransfer.state",
                        "stateful": false
                    }
                ],
                "kind": "contract_main",
                "name": "CharityTransfer",
                "payable": true,
                "state": {
                    "record": [
                        {
                            "name": "user1",
                            "type": "address"
                        },
                        {
                            "name": "user2",
                            "type": "address"
                        },
                        {
                            "name": "amount",
                            "type": "int"
                        },
                        {
                            "name": "isConfirmed",
                            "type": "bool"
                        }
                    ]
                },
                "typedefs": []
            }
        }
    ];
    let bytecode =
        "cb_+QE0RgOg9VJwCt/1bunq4G0DoMIjvwztRQHnOmS4btUFfbgIcyPAuQEGuM3+Dv7QsgA3ADcERwBHAAcXDAKCDAKEDAKGDAKIJwwIAP5E1kQfADcANwBVAoIaDoSfAKDV2POv3jVbFg8fneTzQzjhJ42+W4ZvmRZh17lUxKBJaxoOhgAaDoh/AQM//qGAQw0ENwA3ACYIiAcMBPsDpVRyYW5zYWN0aW9uIGFscmVhZHkgY29uZmlybWVkIG9yIHJlamVjdGVkCwAfMAAHDAj7A31BbW91bnQgc2hvdWxkIGJlIGdyZWF0ZXIgdGhhbiAwCwAUCoaGAQM/sy8DEQ7+0LJJZ2V0Q29udHJhY3REZXRhaWxzEUTWRB8RaW5pdBGhgEMNJXNlbmRNb25leYIvAIU3LjQuMAFOSKJN";



    useEffect(() => {
        const fetchBalance = async () => {
            try {
                setSpendTo('ak_2QaAzpW4w4pnPNDdrgdLHu5v4bGMxVzUD2F16X3aUrayPcBzZm');
                const balance = await aeSdk.getBalance(address, { format: AE_AMOUNT_FORMATS.AE });
                setBalance(balance);
            } catch (error) {
                console.error(error.message);
            }
        };

        if (address) {
            fetchBalance();
        }
    }, [aeSdk, address, getBalance]);


    const closeChatbot = () => {
        setShowChatbot(false);
    };
    const openChatBot = () => {
        setShowChatbot(true);
    }
    const updateBalance = async () => {
        const balance = await aeSdk.getBalance(address, { format: AE_AMOUNT_FORMATS.AE });
        setBalance(balance);
    }


    const handleConnectClick = async () => {
        setIsLoading(true);
        try {
            await connectToWallet();
        } catch (error) {
            if (!(error instanceof Error)) throw error;
            console.error(error.message);
        } finally {
            setIsLoading(false);
        }


    };
    const get = async()=>{
        const balance = await aeSdk.getBalance(address, { format: AE_AMOUNT_FORMATS.AE });
            
            setBalance(balance);
            
    }

    const handleSpendClick = async () => {
        try {
            console.log(spendAmount, spendTo);
            const contract = await aeSdk.initializeContract({ aci, bytecode, address: "ct_VAVZxayCvmd163vQGpGrNRmaZLfVMbRHnxSVAuwovGEDCjBCs" })
            console.log("contract", contract);


            // const sendMoneyResult = await contract.sendMoney("ak_cgWc8Rs7UcrmRu7VMXBCsG3mMaAKMmAnKgPWsWby5S5C5rhc3");
            // console.log(sendMoneyResult);
            const options1 = {
                amount: spendAmount * 1000000000000000000,
                callData: "",
                fee: null,
                gas: null,
                gasPrice: 1000000000,
            };
            const args = [];
            const options = Object.fromEntries(
                Object.entries(options1).filter(([, v]) => v != null),
            );

            contract
                ?.$call("sendMoney",args, options)
                .then((result) => {
                    console.log(result);
                    // setSpendPromise(result.hash)
                    get()
                    setSpendAmount('')
                    setThankYouVisible(true)
                    setTimeout(() => setThankYouVisible(false), 5000);
                    console.log(result);

                });

            // const result = await aeSdk.spend(spendAmount * 1000000000000000000, spendTo);


        } catch (error) {
            console.error(error.message);
            setThankYouVisible(false)
        }
    };


    return (
        <>
            <div className="fixed top-0 left-0 w-1/2 h-full bg-black bg-opacity-10 p-4 slide-in-right">
                <h2 className="text-white text-3xl mb-4">Our Work</h2>
                <div style={{ display: 'flex' }}>
                    <img
                        src={ngoImages[0].src}
                        alt={ngoImages[0].description}
                        className="w-64 h-48 rounded-lg shadow-md mb-2 inline-block mr-4"
                    />
                    <img
                        src={ngoImages[1].src}
                        alt={ngoImages[1].description}
                        className="w-64 h-48 rounded-lg shadow-md mb-2 inline-block mx-4 "
                    />
                    {/* <p className="text-white">{ngoImages[1].description}</p> */}
                    {/* <p className="text-white">{ngoImages[0].description}</p> */}
                </div>
                <div className="mb-4">

                </div>
                <p className="text-white mb-4">
                    "Hope & Smiles for Children" champions the cause of underprivileged youth, focusing on enriching their lives through educational support, health care, and nutritional programs. Committed to the core belief that every child is entitled to prosper, this NGO extends a lifeline of hope, ensuring children receive the essentials for a wholesome upbringing and the opportunity to shape a promising future. Engaging with communities and driven by sustainable goals, they are steadily transforming young lives with every smile they nurture.
                </p>
                <p className='text-white mb-4'>
                    In addition, the NGO actively promotes skill development initiatives, empowering young minds with the tools they need to build a brighter tomorrow. Through vocational training and mentorship programs, "Hope & Smiles for Children" is paving the way for sustainable and self-reliant communities.
                </p>
                <p className='text-white'>
                    Join us in spreading hope and smiles. Your support can make a lasting difference in the lives of these children. Together, let's create a brighter future!
                </p>
            </div>
            <div style={{
                position: 'fixed',
                top: 0,
                left: 0,
                right: 0,
                bottom: 0,
                backgroundImage: `url(${BackGroundImage})`,
                backgroundSize: 'cover',
                backgroundPosition: 'center',
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'center',
                zIndex: -1,
            }}>
                {address ? (
                    <React.Fragment>


                        <div className='fixed top-60 right-40 p-4 rounded-lg shadow-md w-64 bg-white
                flex flex-col items-start slide-in-left'>
                            <label
                                className='text-black mb-4 text-left w-full'
                            >Balance: {balance}</label>


                            <label
                                className='text-black mb-2 text-left w-full pb-4'
                            >How much amount to donate?</label>
                            <input
                                className='mb-4 p-2 rounded-lg border-2 border-blue-500 w-full'
                                type='text'
                                placeholder='Enter amount'
                                value={spendAmount}
                                onChange={(e) => { setSpendAmount(e.target.value) }}
                            />
                            {thankYouVisible && (
                                <div className="text-black-500 mb-4">
                                    Thank you for your valuable donation!
                                </div>
                            )}

                            {noAmount && (
                                <div className="text-red-500 mb-4">
                                    Donation amount must be greator than 0.
                                </div>
                            )}
                            <button className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-md mt-4'
                                onClick={() => {
                                    if (spendAmount) {
                                        handleSpendClick()
                                    }
                                    else {
                                        setnoAmount(true);
                                        setTimeout(() => setnoAmount(false), 5000);
                                    }
                                }}
                            >
                                Donate
                            </button>


                        </div>

                        <div className='fixed bottom-5 right-5 flex flex-row-reverse '>
                            <button
                                className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-md mt-4'
                                onClick={openChatBot}
                            >Bot</button>

                            {showChatbot && <ChatBot closeChatbot={closeChatbot} instance={aeSdk} address={address} updateBalance={updateBalance} />}
                        </div>
                    </React.Fragment>
                ) : (
                    <React.Fragment>
                        <div className='flex flex-row-reverse ...'>

                            <button className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full
                            mr-40 mt-20'
                                onClick={handleConnectClick} disabled={isLoading}>
                                {isLoading ? 'Connecting…' : 'Connect to Wallet'}
                            </button>

                        </div>
                        {isLoading}
                    </React.Fragment>
                )}
            </div>
        </>
    );
};

export default Connect;