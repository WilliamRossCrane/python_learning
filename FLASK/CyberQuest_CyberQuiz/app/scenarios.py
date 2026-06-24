SCENARIOS = [
    {
        "id": 1,
        "title": "Suspicious School Email",
        "topic": "Phishing",
        "situation": "You receive an email saying your school account will be deleted unless you click a link and log in immediately.",
        "choices": [
            {
                "text": "Click the link and log in quickly.",
                "score": 0,
                "feedback": "Risky choice. Phishing emails often create urgency to trick people into clicking fake links.",
            },
            {
                "text": "Check the sender address and report the email to a teacher or IT support.",
                "score": 2,
                "feedback": "Great choice. Checking the sender and reporting suspicious messages is a safe response.",
            },
            {
                "text": "Forward the email to your friends so they know about it.",
                "score": 1,
                "feedback": "Partly helpful, but forwarding suspicious emails can spread unsafe links. It is better to report it.",
            },
        ],
    },
    {
        "id": 2,
        "title": "MFA Code Request",
        "topic": "Multi-Factor Authentication",
        "situation": "Someone messages you saying they are from tech support and need your MFA code to fix your account.",
        "choices": [
            {
                "text": "Send them the code because they said they are from tech support.",
                "score": 0,
                "feedback": "Unsafe choice. MFA codes should never be shared. Attackers may pretend to be trusted people.",
            },
            {
                "text": "Ignore the message and tell a teacher or trusted adult.",
                "score": 2,
                "feedback": "Excellent choice. MFA helps protect accounts, but only if the code stays private.",
            },
            {
                "text": "Ask them why they need it first.",
                "score": 1,
                "feedback": "Questioning the request is better than sending it, but you should still never share MFA codes.",
            },
        ],
    },
    {
        "id": 3,
        "title": "Password Reuse",
        "topic": "Passwords",
        "situation": "You are making a new gaming account. You want to use the same password as your school account so it is easy to remember.",
        "choices": [
            {
                "text": "Use the same password for both accounts.",
                "score": 0,
                "feedback": "Risky choice. If one account is compromised, other accounts using the same password can be at risk too.",
            },
            {
                "text": "Use a unique passphrase for the gaming account.",
                "score": 2,
                "feedback": "Great choice. Unique passphrases help protect your accounts.",
            },
            {
                "text": "Use your name and birthday so you remember it.",
                "score": 0,
                "feedback": "Unsafe choice. Personal information can be easy for others to guess.",
            },
        ],
    },
    {
        "id": 4,
        "title": "App Permissions",
        "topic": "Digital Footprint",
        "situation": "A free wallpaper app asks for access to your location, contacts, camera, and microphone.",
        "choices": [
            {
                "text": "Allow everything so the app works properly.",
                "score": 0,
                "feedback": "Risky choice. Apps should only collect data they actually need.",
            },
            {
                "text": "Check why the app needs those permissions and deny anything unnecessary.",
                "score": 2,
                "feedback": "Excellent choice. Managing app permissions helps reduce your digital footprint.",
            },
            {
                "text": "Allow location only because that seems harmless.",
                "score": 1,
                "feedback": "Better than allowing everything, but you should still ask whether the app really needs location data.",
            },
        ],
    },
    {
        "id": 5,
        "title": "Public Wi-Fi",
        "topic": "Network Safety",
        "situation": "You are at a shopping centre and see free public Wi-Fi. You want to log in to an important account.",
        "choices": [
            {
                "text": "Log in straight away because the Wi-Fi is free.",
                "score": 0,
                "feedback": "Risky choice. Public Wi-Fi can be less secure, especially for important accounts.",
            },
            {
                "text": "Wait until you are on a trusted network or use safer options if available.",
                "score": 2,
                "feedback": "Good choice. It is safer to use trusted networks for important accounts.",
            },
            {
                "text": "Ask a friend if they have used the Wi-Fi before.",
                "score": 1,
                "feedback": "Asking can help, but it does not guarantee the network is secure.",
            },
        ],
    },
]