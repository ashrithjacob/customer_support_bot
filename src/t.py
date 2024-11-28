j = [
    {
        "stream": True,
        "model": "test",
        "messages": [{"role": "user", "content": "ooooo"}],
        "files": [
            {
                "type": "file",
                "file": {
                    "id": "4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                    "user_id": "c7ea8c60-03e4-4828-b497-501f94695277",
                    "hash": "8a2710bb5ee383408d9507f25dc4549c7b8d24aab763ea42caa44898ae7b49ac",
                    "filename": "test_txt.txt",
                    "data": {
                        "content": "EDUCATION\nTechnical University, Dortmund\nJul 2019 - Dec 2020\nMaster's thesis project on \"Increasing transverse relaxation (T2) in magnetic resonance imaging\"\nDesigned pulse sequences on Bruker scanners to improve image resolution of MRI images by prolonging the transverse\nrelaxation by the addition of π refocusing pulses and wrote image processing scripts in MATLAB to create 'noise\nmasks' to render the MRI image, background noise free\nIndian Institute for Science Education and Research, Pune\n2015 - 2020\nBS-MS dual degree in physics (minor mathematics). Courses included: Statistical mechanics, Non-linear dynamics,\nLinear algebra, Quantum mechanics, Graph theory, Cryptography, Data Science, Probability and Statistics\nCGPA: 8.9/10\nTECHNOLOGY STACK\nMachine learning libraries: Pytorch, mlflow, NumPy, Pandas, scikit-learn, XGboost, Langchain\nProgramming Languages: Python, SQL, Fortran,LATEX, HTML, CSS\nOthers: FastAPI, Flask, Docker, Docker-Compose, Ansible, AWS(Sagemaker, s3, EC2), Bash, Git, DICOM(Digital\nImaging and Communications in Medicine)\nWORK EXPERIENCE\nAI Consultant- Gateway ventures\nDec 2022 - present\nNLP: RAG/ Autonomous Agents\nBangalore, India\n• Built a RAG + Knowledge graph pipeline with vision transformer models to extract context from video data\nextracted from wearables to serve as a AI personal assistant. Worked with a product manager to align tasks\nand objectives and implement design.\n• Worked closely with external clients for chatbot development: Built and hosted a website for customers to\nleverage OpenAI's API to summarise and answer questions on larger documents. Sped up large document perusal\nfor client by 10x(langchain, fastapi, gpt-4). Further Fine-tuned a custom chatbot based on the client's proprietary\ndata and weblinks, using LLamaIndex for retrieval augmented generation(RAG) to generate a non-hallucinating\nresponse, based on custom corpus of data (tech used: LLamaIndex, gpt4, text embeddings, streamlit).\n• developed an ML pipeline to generate consumer behaviour insight from video data for an ecommerce company\nto improve targetted advertisements for the client.\nMediaire Gmbh\nJul 2022 - Nov 2022\nML engineer/ Customer Support\nBerlin, Germany\nMediaire is a startup building AI products for MRI such as image segmentations and automated diagnostic reports.\nAs part of the early team, was involved in support and data roles\n• as part of the ML team helped fine-tune nnunet for knee and prostate data. Fine tuning involved choice of\nempirical parameters(3D v 2D v 3D cascade for the specific use case), improving eval metric(dice coefficient) by\n7%.\n• Streamlining customer support: creating bug reports, debugging client issues using logs and database queries(sqlite),\ndeveloping structured processes in developing workflows for the customer success team.\n• Tested and secured client connections through a bastion server using Ansible, employing infrastructure as code\nMax Delbruck Center for Molecular Medicine\nSep 2021 - Mar 2022\nResearch Intern\nBerlin, Germany\nMDC is a research institute partnering with industry, dedicated to solving problems in healthcare and biotech- nology\n• Developed data processing pipelines to implement the following: 1. First and Second order phase corrections on\nMRI data. 2. Data cleansing to eliminate background noise thus rendering the highest sharpness of images for\nML pipeline(segmentation, detection etc.)\nSCHOLARSHIPS AND AWARDS\nKVPY Scholarship, awarded by Indian Institute of Science: Undergraduate science scholarship awarded\nwith acceptance rate < 0.5%\n(2014)\nINSPIRE Scholarship for Merit, awarded by Central Board for Secondary Education(CBSE): Awarded\nfor being in the top 0.1% of students in the country at mathematics\n(2015)\n"
                    },
                    "meta": {
                        "name": "test_txt.txt",
                        "content_type": "text/plain",
                        "size": 3757,
                        "collection_name": "file-4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                    },
                    "created_at": 1732534506,
                    "updated_at": 1732534506,
                },
                "id": "4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                "url": "/api/v1/files/4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                "name": "test_txt.txt",
                "collection_name": "file-4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                "status": "uploaded",
                "size": 3757,
                "error": "",
                "itemId": "8c2aed8e-520c-4a8e-ab34-1537cf9d7ce8",
            }
        ],
        "session_id": "dJp3AZ2TJsl3NDOfAAAB",
        "chat_id": "447c1e87-6ab1-4622-9f4d-025deec73752",
        "id": "215657db-7ec7-40b8-bd07-f3c26c769215",
    },
    {
        "model": "test",
        "messages": [
            {
                "role": "user",
                "content": '### Task:\nBased on the chat history, determine whether a search is necessary, and if so, generate a 1-3 broad search queries to retrieve comprehensive and updated information. If no search is required, return an empty list.\n\n### Guidelines:\n- Respond exclusively with a JSON object.\n- If a search query is needed, return an object like: { "queries": ["query1", "query2"] } where each query is distinct and concise.\n- If no search query is necessary, output should be: { "queries": [] }\n- Default to suggesting a search query to ensure accurate and updated information, unless it is definitively clear no search is required.\n- Be concise, focusing strictly on composing search queries with no additional commentary or text.\n- When in doubt, prefer to suggest a search for comprehensiveness.\n- Today\'s date is: 2024-11-25\n\n### Output:\nJSON format: {\n  "queries": ["query1", "query2"]\n}\n\n### Chat History:\n<chat_history>\nUSER: ooooo\n</chat_history>\n',
            }
        ],
        "stream": False,
        "metadata": {
            "task": "query_generation",
            "task_body": {
                "model": "test",
                "messages": [{"role": "user", "content": "ooooo"}],
                "type": "retrieval",
            },
        },
    },
    {
        "model": "test",
        "messages": [
            {
                "role": "user",
                "content": "Create a concise, 3-5 word title with an emoji as a title for the chat history, in the given language. Suitable Emojis for the summary can be used to enhance understanding but avoid quotation marks or special formatting. RESPOND ONLY WITH THE TITLE TEXT.\n\nExamples of titles:\n📉 Stock Market Trends\n🍪 Perfect Chocolate Chip Recipe\nEvolution of Music Streaming\nRemote Work Productivity Tips\nArtificial Intelligence in Healthcare\n🎮 Video Game Development Insights\n\n<chat_history>\nUSER: ooooo\nASSISTANT: {'stream': True, 'model': 'test', 'messages': [{'role': 'system', 'content': '### Task:\\nRespond to the user query using the provided context, incorporating inline citations in the format [source_id] **only when the <source_id> tag is explicitly provided** in the context.\\n\\n### Guidelines:\\n- If you don\\'t know the answer, clearly state that.\\n- If uncertain, ask the user for clarification.\\n- Respond in the same language as the user\\'s query.\\n- If the context is unreadable or of poor quality, inform the user and provide the best possible answer.\\n- If the answer isn\\'t present in the context but you possess the knowledge, explain this to the user and provide the answer using your own understanding.\\n- **Only include inline citations using [source_id] when a <source_id> tag is explicitly provided in the context.**  \\n- Do not cite if the <source_id> tag is not provided in the context.  \\n- Do not use XML tags in your response.\\n- Ensure citations are concise and directly related to the information provided.\\n\\n### Example of Citation:\\nIf the user asks about a specific topic and the information is found in \"whitepaper.pdf\" with a provided <source_id>, the response should include the citation like so:  \\n* \"According to the study, the proposed method increases efficiency by 20% [whitepaper.pdf].\"\\nIf no <source_id> is present, the response should omit the citation.\\n\\n### Output:\\nProvide a clear and direct response to the user\\'s query, including inline citations in the format [source_id] only when the <source_id> tag is present in the context.\\n\\n<context>\\n<source><source_id>test_txt.txt</source_id><source_context>for being in the top 0.1% of students in the country at mathematics\\n(2015)</source_context></source>\\n<source><source_id>test_txt.txt</source_id><source_context>EDUCATION\\nTechnical University, Dortmund\\nJul 2019 - Dec 2020\\nMaster\\'s thesis project on \"Increasing transverse relaxation (T2) in magnetic resonance imaging\"\\nDesigned pulse sequences on Bruker scanners to improve image resolution of MRI images by prolonging the transverse\\nrelaxation by the addition of π refocusing pulses and wrote image processing scripts in MATLAB to create \\'noise\\nmasks\\' to render the MRI image, background noise free\\nIndian Institute for Science Education and Research, Pune\\n2015 - 2020\\nBS-MS dual degree in physics (minor mathematics). Courses included: Statistical mechanics, Non-linear dynamics,\\nLinear algebra, Quantum mechanics, Graph theory, Cryptography, Data Science, Probability and Statistics\\nCGPA: 8.9/10\\nTECHNOLOGY STACK\\nMachine learning libraries: Pytorch, mlflow, NumPy, Pandas, scikit-learn, XGboost, Langchain\\nProgramming Languages: Python, SQL, Fortran,LATEX, HTML, CSS</source_context></source>\\n<source><source_id>test_txt.txt</source_id><source_context>data and weblinks, using LLamaIndex for retrieval augmented generation(RAG) to generate a non-hallucinating\\nresponse, based on custom corpus of data (tech used: LLamaIndex, gpt4, text embeddings, streamlit).\\n• developed an ML pipeline to generate consumer behaviour insight from video data for an ecommerce company\\nto improve targetted advertisements for the client.\\nMediaire Gmbh\\nJul 2022 - Nov 2022\\nML engineer/ Customer Support\\nBerlin, Germany\\nMediaire is a startup building AI products for MRI such as image segmentations and automated diagnostic reports.\\nAs part of the early team, was involved in support and data roles\\n• as part of the ML team helped fine-tune nnunet for knee and prostate data. Fine tuning involved choice of\\nempirical parameters(3D v 2D v 3D cascade for the specific use case), improving eval metric(dice coefficient) by\\n7%.\\n• Streamlining customer support: creating bug reports, debugging client issues using logs and database queries(sqlite),</source_context></source>\\n</context>\\n\\n<user_query>\\nooooo\\n</user_query>\\n'}, {'role': 'user', 'content': 'ooooo'}], 'user': {'name': 'Ashjack', 'id': 'c7ea8c60-03e4-4828-b497-501f94695277', 'email': 'ashrithjacob2@gmail.com', 'role': 'admin'}}\n</chat_history>",
            }
        ],
        "stream": False,
        "max_completion_tokens": 50,
        "chat_id": "447c1e87-6ab1-4622-9f4d-025deec73752",
        "metadata": {
            "task": "title_generation",
            "task_body": {
                "model": "test",
                "messages": [
                    {
                        "id": "59a20c91-6e3a-4e7f-8e6b-f9bb86454db3",
                        "parentId": None,
                        "childrenIds": ["215657db-7ec7-40b8-bd07-f3c26c769215"],
                        "role": "user",
                        "content": "ooooo",
                        "files": [
                            {
                                "type": "file",
                                "file": {
                                    "id": "4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                                    "user_id": "c7ea8c60-03e4-4828-b497-501f94695277",
                                    "hash": "8a2710bb5ee383408d9507f25dc4549c7b8d24aab763ea42caa44898ae7b49ac",
                                    "filename": "test_txt.txt",
                                    "data": {
                                        "content": "EDUCATION\nTechnical University, Dortmund\nJul 2019 - Dec 2020\nMaster's thesis project on \"Increasing transverse relaxation (T2) in magnetic resonance imaging\"\nDesigned pulse sequences on Bruker scanners to improve image resolution of MRI images by prolonging the transverse\nrelaxation by the addition of π refocusing pulses and wrote image processing scripts in MATLAB to create 'noise\nmasks' to render the MRI image, background noise free\nIndian Institute for Science Education and Research, Pune\n2015 - 2020\nBS-MS dual degree in physics (minor mathematics). Courses included: Statistical mechanics, Non-linear dynamics,\nLinear algebra, Quantum mechanics, Graph theory, Cryptography, Data Science, Probability and Statistics\nCGPA: 8.9/10\nTECHNOLOGY STACK\nMachine learning libraries: Pytorch, mlflow, NumPy, Pandas, scikit-learn, XGboost, Langchain\nProgramming Languages: Python, SQL, Fortran,LATEX, HTML, CSS\nOthers: FastAPI, Flask, Docker, Docker-Compose, Ansible, AWS(Sagemaker, s3, EC2), Bash, Git, DICOM(Digital\nImaging and Communications in Medicine)\nWORK EXPERIENCE\nAI Consultant- Gateway ventures\nDec 2022 - present\nNLP: RAG/ Autonomous Agents\nBangalore, India\n• Built a RAG + Knowledge graph pipeline with vision transformer models to extract context from video data\nextracted from wearables to serve as a AI personal assistant. Worked with a product manager to align tasks\nand objectives and implement design.\n• Worked closely with external clients for chatbot development: Built and hosted a website for customers to\nleverage OpenAI's API to summarise and answer questions on larger documents. Sped up large document perusal\nfor client by 10x(langchain, fastapi, gpt-4). Further Fine-tuned a custom chatbot based on the client's proprietary\ndata and weblinks, using LLamaIndex for retrieval augmented generation(RAG) to generate a non-hallucinating\nresponse, based on custom corpus of data (tech used: LLamaIndex, gpt4, text embeddings, streamlit).\n• developed an ML pipeline to generate consumer behaviour insight from video data for an ecommerce company\nto improve targetted advertisements for the client.\nMediaire Gmbh\nJul 2022 - Nov 2022\nML engineer/ Customer Support\nBerlin, Germany\nMediaire is a startup building AI products for MRI such as image segmentations and automated diagnostic reports.\nAs part of the early team, was involved in support and data roles\n• as part of the ML team helped fine-tune nnunet for knee and prostate data. Fine tuning involved choice of\nempirical parameters(3D v 2D v 3D cascade for the specific use case), improving eval metric(dice coefficient) by\n7%.\n• Streamlining customer support: creating bug reports, debugging client issues using logs and database queries(sqlite),\ndeveloping structured processes in developing workflows for the customer success team.\n• Tested and secured client connections through a bastion server using Ansible, employing infrastructure as code\nMax Delbruck Center for Molecular Medicine\nSep 2021 - Mar 2022\nResearch Intern\nBerlin, Germany\nMDC is a research institute partnering with industry, dedicated to solving problems in healthcare and biotech- nology\n• Developed data processing pipelines to implement the following: 1. First and Second order phase corrections on\nMRI data. 2. Data cleansing to eliminate background noise thus rendering the highest sharpness of images for\nML pipeline(segmentation, detection etc.)\nSCHOLARSHIPS AND AWARDS\nKVPY Scholarship, awarded by Indian Institute of Science: Undergraduate science scholarship awarded\nwith acceptance rate < 0.5%\n(2014)\nINSPIRE Scholarship for Merit, awarded by Central Board for Secondary Education(CBSE): Awarded\nfor being in the top 0.1% of students in the country at mathematics\n(2015)\n"
                                    },
                                    "meta": {
                                        "name": "test_txt.txt",
                                        "content_type": "text/plain",
                                        "size": 3757,
                                        "collection_name": "file-4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                                    },
                                    "created_at": 1732534506,
                                    "updated_at": 1732534506,
                                },
                                "id": "4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                                "url": "/api/v1/files/4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                                "name": "test_txt.txt",
                                "collection_name": "file-4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                                "status": "uploaded",
                                "size": 3757,
                                "error": "",
                                "itemId": "8c2aed8e-520c-4a8e-ab34-1537cf9d7ce8",
                            }
                        ],
                        "timestamp": 1732534510,
                        "models": ["test"],
                    },
                    {
                        "parentId": "59a20c91-6e3a-4e7f-8e6b-f9bb86454db3",
                        "id": "215657db-7ec7-40b8-bd07-f3c26c769215",
                        "childrenIds": [],
                        "role": "assistant",
                        "content": "{'stream': True, 'model': 'test', 'messages': [{'role': 'system', 'content': '### Task:\\nRespond to the user query using the provided context, incorporating inline citations in the format [source_id] **only when the <source_id> tag is explicitly provided** in the context.\\n\\n### Guidelines:\\n- If you don\\'t know the answer, clearly state that.\\n- If uncertain, ask the user for clarification.\\n- Respond in the same language as the user\\'s query.\\n- If the context is unreadable or of poor quality, inform the user and provide the best possible answer.\\n- If the answer isn\\'t present in the context but you possess the knowledge, explain this to the user and provide the answer using your own understanding.\\n- **Only include inline citations using [source_id] when a <source_id> tag is explicitly provided in the context.**  \\n- Do not cite if the <source_id> tag is not provided in the context.  \\n- Do not use XML tags in your response.\\n- Ensure citations are concise and directly related to the information provided.\\n\\n### Example of Citation:\\nIf the user asks about a specific topic and the information is found in \"whitepaper.pdf\" with a provided <source_id>, the response should include the citation like so:  \\n* \"According to the study, the proposed method increases efficiency by 20% [whitepaper.pdf].\"\\nIf no <source_id> is present, the response should omit the citation.\\n\\n### Output:\\nProvide a clear and direct response to the user\\'s query, including inline citations in the format [source_id] only when the <source_id> tag is present in the context.\\n\\n<context>\\n<source><source_id>test_txt.txt</source_id><source_context>for being in the top 0.1% of students in the country at mathematics\\n(2015)</source_context></source>\\n<source><source_id>test_txt.txt</source_id><source_context>EDUCATION\\nTechnical University, Dortmund\\nJul 2019 - Dec 2020\\nMaster\\'s thesis project on \"Increasing transverse relaxation (T2) in magnetic resonance imaging\"\\nDesigned pulse sequences on Bruker scanners to improve image resolution of MRI images by prolonging the transverse\\nrelaxation by the addition of π refocusing pulses and wrote image processing scripts in MATLAB to create \\'noise\\nmasks\\' to render the MRI image, background noise free\\nIndian Institute for Science Education and Research, Pune\\n2015 - 2020\\nBS-MS dual degree in physics (minor mathematics). Courses included: Statistical mechanics, Non-linear dynamics,\\nLinear algebra, Quantum mechanics, Graph theory, Cryptography, Data Science, Probability and Statistics\\nCGPA: 8.9/10\\nTECHNOLOGY STACK\\nMachine learning libraries: Pytorch, mlflow, NumPy, Pandas, scikit-learn, XGboost, Langchain\\nProgramming Languages: Python, SQL, Fortran,LATEX, HTML, CSS</source_context></source>\\n<source><source_id>test_txt.txt</source_id><source_context>data and weblinks, using LLamaIndex for retrieval augmented generation(RAG) to generate a non-hallucinating\\nresponse, based on custom corpus of data (tech used: LLamaIndex, gpt4, text embeddings, streamlit).\\n• developed an ML pipeline to generate consumer behaviour insight from video data for an ecommerce company\\nto improve targetted advertisements for the client.\\nMediaire Gmbh\\nJul 2022 - Nov 2022\\nML engineer/ Customer Support\\nBerlin, Germany\\nMediaire is a startup building AI products for MRI such as image segmentations and automated diagnostic reports.\\nAs part of the early team, was involved in support and data roles\\n• as part of the ML team helped fine-tune nnunet for knee and prostate data. Fine tuning involved choice of\\nempirical parameters(3D v 2D v 3D cascade for the specific use case), improving eval metric(dice coefficient) by\\n7%.\\n• Streamlining customer support: creating bug reports, debugging client issues using logs and database queries(sqlite),</source_context></source>\\n</context>\\n\\n<user_query>\\nooooo\\n</user_query>\\n'}, {'role': 'user', 'content': 'ooooo'}], 'user': {'name': 'Ashjack', 'id': 'c7ea8c60-03e4-4828-b497-501f94695277', 'email': 'ashrithjacob2@gmail.com', 'role': 'admin'}}",
                        "model": "test",
                        "modelName": "test",
                        "modelIdx": 0,
                        "userContext": None,
                        "timestamp": 1732534510,
                        "sources": [
                            {
                                "source": {
                                    "type": "file",
                                    "file": {
                                        "id": "4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                                        "user_id": "c7ea8c60-03e4-4828-b497-501f94695277",
                                        "hash": "8a2710bb5ee383408d9507f25dc4549c7b8d24aab763ea42caa44898ae7b49ac",
                                        "filename": "test_txt.txt",
                                        "data": {
                                            "content": "EDUCATION\nTechnical University, Dortmund\nJul 2019 - Dec 2020\nMaster's thesis project on \"Increasing transverse relaxation (T2) in magnetic resonance imaging\"\nDesigned pulse sequences on Bruker scanners to improve image resolution of MRI images by prolonging the transverse\nrelaxation by the addition of π refocusing pulses and wrote image processing scripts in MATLAB to create 'noise\nmasks' to render the MRI image, background noise free\nIndian Institute for Science Education and Research, Pune\n2015 - 2020\nBS-MS dual degree in physics (minor mathematics). Courses included: Statistical mechanics, Non-linear dynamics,\nLinear algebra, Quantum mechanics, Graph theory, Cryptography, Data Science, Probability and Statistics\nCGPA: 8.9/10\nTECHNOLOGY STACK\nMachine learning libraries: Pytorch, mlflow, NumPy, Pandas, scikit-learn, XGboost, Langchain\nProgramming Languages: Python, SQL, Fortran,LATEX, HTML, CSS\nOthers: FastAPI, Flask, Docker, Docker-Compose, Ansible, AWS(Sagemaker, s3, EC2), Bash, Git, DICOM(Digital\nImaging and Communications in Medicine)\nWORK EXPERIENCE\nAI Consultant- Gateway ventures\nDec 2022 - present\nNLP: RAG/ Autonomous Agents\nBangalore, India\n• Built a RAG + Knowledge graph pipeline with vision transformer models to extract context from video data\nextracted from wearables to serve as a AI personal assistant. Worked with a product manager to align tasks\nand objectives and implement design.\n• Worked closely with external clients for chatbot development: Built and hosted a website for customers to\nleverage OpenAI's API to summarise and answer questions on larger documents. Sped up large document perusal\nfor client by 10x(langchain, fastapi, gpt-4). Further Fine-tuned a custom chatbot based on the client's proprietary\ndata and weblinks, using LLamaIndex for retrieval augmented generation(RAG) to generate a non-hallucinating\nresponse, based on custom corpus of data (tech used: LLamaIndex, gpt4, text embeddings, streamlit).\n• developed an ML pipeline to generate consumer behaviour insight from video data for an ecommerce company\nto improve targetted advertisements for the client.\nMediaire Gmbh\nJul 2022 - Nov 2022\nML engineer/ Customer Support\nBerlin, Germany\nMediaire is a startup building AI products for MRI such as image segmentations and automated diagnostic reports.\nAs part of the early team, was involved in support and data roles\n• as part of the ML team helped fine-tune nnunet for knee and prostate data. Fine tuning involved choice of\nempirical parameters(3D v 2D v 3D cascade for the specific use case), improving eval metric(dice coefficient) by\n7%.\n• Streamlining customer support: creating bug reports, debugging client issues using logs and database queries(sqlite),\ndeveloping structured processes in developing workflows for the customer success team.\n• Tested and secured client connections through a bastion server using Ansible, employing infrastructure as code\nMax Delbruck Center for Molecular Medicine\nSep 2021 - Mar 2022\nResearch Intern\nBerlin, Germany\nMDC is a research institute partnering with industry, dedicated to solving problems in healthcare and biotech- nology\n• Developed data processing pipelines to implement the following: 1. First and Second order phase corrections on\nMRI data. 2. Data cleansing to eliminate background noise thus rendering the highest sharpness of images for\nML pipeline(segmentation, detection etc.)\nSCHOLARSHIPS AND AWARDS\nKVPY Scholarship, awarded by Indian Institute of Science: Undergraduate science scholarship awarded\nwith acceptance rate < 0.5%\n(2014)\nINSPIRE Scholarship for Merit, awarded by Central Board for Secondary Education(CBSE): Awarded\nfor being in the top 0.1% of students in the country at mathematics\n(2015)\n"
                                        },
                                        "meta": {
                                            "name": "test_txt.txt",
                                            "content_type": "text/plain",
                                            "size": 3757,
                                            "collection_name": "file-4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                                        },
                                        "created_at": 1732534506,
                                        "updated_at": 1732534506,
                                    },
                                    "id": "4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                                    "url": "/api/v1/files/4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                                    "name": "test_txt.txt",
                                    "collection_name": "file-4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                                    "status": "uploaded",
                                    "size": 3757,
                                    "error": "",
                                    "itemId": "8c2aed8e-520c-4a8e-ab34-1537cf9d7ce8",
                                },
                                "document": [
                                    "for being in the top 0.1% of students in the country at mathematics\n(2015)",
                                    "EDUCATION\nTechnical University, Dortmund\nJul 2019 - Dec 2020\nMaster's thesis project on \"Increasing transverse relaxation (T2) in magnetic resonance imaging\"\nDesigned pulse sequences on Bruker scanners to improve image resolution of MRI images by prolonging the transverse\nrelaxation by the addition of π refocusing pulses and wrote image processing scripts in MATLAB to create 'noise\nmasks' to render the MRI image, background noise free\nIndian Institute for Science Education and Research, Pune\n2015 - 2020\nBS-MS dual degree in physics (minor mathematics). Courses included: Statistical mechanics, Non-linear dynamics,\nLinear algebra, Quantum mechanics, Graph theory, Cryptography, Data Science, Probability and Statistics\nCGPA: 8.9/10\nTECHNOLOGY STACK\nMachine learning libraries: Pytorch, mlflow, NumPy, Pandas, scikit-learn, XGboost, Langchain\nProgramming Languages: Python, SQL, Fortran,LATEX, HTML, CSS",
                                    "data and weblinks, using LLamaIndex for retrieval augmented generation(RAG) to generate a non-hallucinating\nresponse, based on custom corpus of data (tech used: LLamaIndex, gpt4, text embeddings, streamlit).\n• developed an ML pipeline to generate consumer behaviour insight from video data for an ecommerce company\nto improve targetted advertisements for the client.\nMediaire Gmbh\nJul 2022 - Nov 2022\nML engineer/ Customer Support\nBerlin, Germany\nMediaire is a startup building AI products for MRI such as image segmentations and automated diagnostic reports.\nAs part of the early team, was involved in support and data roles\n• as part of the ML team helped fine-tune nnunet for knee and prostate data. Fine tuning involved choice of\nempirical parameters(3D v 2D v 3D cascade for the specific use case), improving eval metric(dice coefficient) by\n7%.\n• Streamlining customer support: creating bug reports, debugging client issues using logs and database queries(sqlite),",
                                ],
                                "metadata": [
                                    {
                                        "created_by": "c7ea8c60-03e4-4828-b497-501f94695277",
                                        "embedding_config": '{"engine": "", "model": "sentence-transformers/all-MiniLM-L6-v2"}',
                                        "file_id": "4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                                        "hash": "8a2710bb5ee383408d9507f25dc4549c7b8d24aab763ea42caa44898ae7b49ac",
                                        "name": "test_txt.txt",
                                        "source": "test_txt.txt",
                                        "start_index": 3653,
                                    },
                                    {
                                        "created_by": "c7ea8c60-03e4-4828-b497-501f94695277",
                                        "embedding_config": '{"engine": "", "model": "sentence-transformers/all-MiniLM-L6-v2"}',
                                        "file_id": "4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                                        "hash": "8a2710bb5ee383408d9507f25dc4549c7b8d24aab763ea42caa44898ae7b49ac",
                                        "name": "test_txt.txt",
                                        "source": "test_txt.txt",
                                        "start_index": 0,
                                    },
                                    {
                                        "created_by": "c7ea8c60-03e4-4828-b497-501f94695277",
                                        "embedding_config": '{"engine": "", "model": "sentence-transformers/all-MiniLM-L6-v2"}',
                                        "file_id": "4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                                        "hash": "8a2710bb5ee383408d9507f25dc4549c7b8d24aab763ea42caa44898ae7b49ac",
                                        "name": "test_txt.txt",
                                        "source": "test_txt.txt",
                                        "start_index": 1751,
                                    },
                                ],
                                "distances": [
                                    0.8640056863409906,
                                    0.908019051016864,
                                    0.9489762110419019,
                                ],
                            }
                        ],
                        "lastSentence": "Courses included: Statistical mechanics, Non-linear dynamics,\\nLinear algebra, Quantum mechanics, Graph theory, Cryptography, Data Science, Probability and Statistics\\nCGPA: 8.9/10\\nTECHNOLOGY STACK\\nMachine learning libraries: Pytorch, mlflow, NumPy, Pandas, scikit-learn, XGboost, Langchain\\nProgramming Languages: Python, SQL, Fortran,LATEX, HTML, CSS</source_context></source>\\n<source><source_id>test_txt.txt</source_id><source_context>data and weblinks, using LLamaIndex for retrieval augmented generation(RAG) to generate a non-hallucinating\\nresponse, based on custom corpus of data (tech used: LLamaIndex, gpt4, text embeddings, streamlit).\\n• developed an ML pipeline to generate consumer behaviour insight from video data for an ecommerce company\\nto improve targetted advertisements for the client.\\nMediaire Gmbh\\nJul 2022 - Nov 2022\\nML engineer/ Customer Support\\nBerlin, Germany\\nMediaire is a startup building AI products for MRI such as image segmentations and automated diagnostic reports.\\nAs part of the early team, was involved in support and data roles\\n• as part of the ML team helped fine-tune nnunet for knee and prostate data.",
                        "done": True,
                    },
                ],
                "chat_id": "447c1e87-6ab1-4622-9f4d-025deec73752",
            },
        },
    },
    {
        "model": "test",
        "messages": [
            {
                "role": "user",
                "content": "### Task:\nGenerate 1-3 broad tags categorizing the main themes of the chat history, along with 1-3 more specific subtopic tags.\n\n### Guidelines:\n- Start with high-level domains (e.g. Science, Technology, Philosophy, Arts, Politics, Business, Health, Sports, Entertainment, Education)\n- Consider including relevant subfields/subdomains if they are strongly represented throughout the conversation\n- If content is too short (less than 3 messages) or too diverse, use only [\"General\"]\n- Use the chat's primary language; default to English if multilingual\n- Prioritize accuracy over specificity\n\n### Output:\nJSON format: { \"tags\": [\"tag1\", \"tag2\", \"tag3\"] }\n\n### Chat History:\n<chat_history>\nUSER: ooooo\nASSISTANT: {'stream': True, 'model': 'test', 'messages': [{'role': 'system', 'content': '### Task:\\nRespond to the user query using the provided context, incorporating inline citations in the format [source_id] **only when the <source_id> tag is explicitly provided** in the context.\\n\\n### Guidelines:\\n- If you don\\'t know the answer, clearly state that.\\n- If uncertain, ask the user for clarification.\\n- Respond in the same language as the user\\'s query.\\n- If the context is unreadable or of poor quality, inform the user and provide the best possible answer.\\n- If the answer isn\\'t present in the context but you possess the knowledge, explain this to the user and provide the answer using your own understanding.\\n- **Only include inline citations using [source_id] when a <source_id> tag is explicitly provided in the context.**  \\n- Do not cite if the <source_id> tag is not provided in the context.  \\n- Do not use XML tags in your response.\\n- Ensure citations are concise and directly related to the information provided.\\n\\n### Example of Citation:\\nIf the user asks about a specific topic and the information is found in \"whitepaper.pdf\" with a provided <source_id>, the response should include the citation like so:  \\n* \"According to the study, the proposed method increases efficiency by 20% [whitepaper.pdf].\"\\nIf no <source_id> is present, the response should omit the citation.\\n\\n### Output:\\nProvide a clear and direct response to the user\\'s query, including inline citations in the format [source_id] only when the <source_id> tag is present in the context.\\n\\n<context>\\n<source><source_id>test_txt.txt</source_id><source_context>for being in the top 0.1% of students in the country at mathematics\\n(2015)</source_context></source>\\n<source><source_id>test_txt.txt</source_id><source_context>EDUCATION\\nTechnical University, Dortmund\\nJul 2019 - Dec 2020\\nMaster\\'s thesis project on \"Increasing transverse relaxation (T2) in magnetic resonance imaging\"\\nDesigned pulse sequences on Bruker scanners to improve image resolution of MRI images by prolonging the transverse\\nrelaxation by the addition of π refocusing pulses and wrote image processing scripts in MATLAB to create \\'noise\\nmasks\\' to render the MRI image, background noise free\\nIndian Institute for Science Education and Research, Pune\\n2015 - 2020\\nBS-MS dual degree in physics (minor mathematics). Courses included: Statistical mechanics, Non-linear dynamics,\\nLinear algebra, Quantum mechanics, Graph theory, Cryptography, Data Science, Probability and Statistics\\nCGPA: 8.9/10\\nTECHNOLOGY STACK\\nMachine learning libraries: Pytorch, mlflow, NumPy, Pandas, scikit-learn, XGboost, Langchain\\nProgramming Languages: Python, SQL, Fortran,LATEX, HTML, CSS</source_context></source>\\n<source><source_id>test_txt.txt</source_id><source_context>data and weblinks, using LLamaIndex for retrieval augmented generation(RAG) to generate a non-hallucinating\\nresponse, based on custom corpus of data (tech used: LLamaIndex, gpt4, text embeddings, streamlit).\\n• developed an ML pipeline to generate consumer behaviour insight from video data for an ecommerce company\\nto improve targetted advertisements for the client.\\nMediaire Gmbh\\nJul 2022 - Nov 2022\\nML engineer/ Customer Support\\nBerlin, Germany\\nMediaire is a startup building AI products for MRI such as image segmentations and automated diagnostic reports.\\nAs part of the early team, was involved in support and data roles\\n• as part of the ML team helped fine-tune nnunet for knee and prostate data. Fine tuning involved choice of\\nempirical parameters(3D v 2D v 3D cascade for the specific use case), improving eval metric(dice coefficient) by\\n7%.\\n• Streamlining customer support: creating bug reports, debugging client issues using logs and database queries(sqlite),</source_context></source>\\n</context>\\n\\n<user_query>\\nooooo\\n</user_query>\\n'}, {'role': 'user', 'content': 'ooooo'}], 'user': {'name': 'Ashjack', 'id': 'c7ea8c60-03e4-4828-b497-501f94695277', 'email': 'ashrithjacob2@gmail.com', 'role': 'admin'}}\n</chat_history>",
            }
        ],
        "stream": False,
        "metadata": {
            "task": "tags_generation",
            "task_body": {
                "model": "test",
                "messages": [
                    {
                        "id": "59a20c91-6e3a-4e7f-8e6b-f9bb86454db3",
                        "parentId": None,
                        "childrenIds": ["215657db-7ec7-40b8-bd07-f3c26c769215"],
                        "role": "user",
                        "content": "ooooo",
                        "files": [
                            {
                                "type": "file",
                                "file": {
                                    "id": "4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                                    "user_id": "c7ea8c60-03e4-4828-b497-501f94695277",
                                    "hash": "8a2710bb5ee383408d9507f25dc4549c7b8d24aab763ea42caa44898ae7b49ac",
                                    "filename": "test_txt.txt",
                                    "data": {
                                        "content": "EDUCATION\nTechnical University, Dortmund\nJul 2019 - Dec 2020\nMaster's thesis project on \"Increasing transverse relaxation (T2) in magnetic resonance imaging\"\nDesigned pulse sequences on Bruker scanners to improve image resolution of MRI images by prolonging the transverse\nrelaxation by the addition of π refocusing pulses and wrote image processing scripts in MATLAB to create 'noise\nmasks' to render the MRI image, background noise free\nIndian Institute for Science Education and Research, Pune\n2015 - 2020\nBS-MS dual degree in physics (minor mathematics). Courses included: Statistical mechanics, Non-linear dynamics,\nLinear algebra, Quantum mechanics, Graph theory, Cryptography, Data Science, Probability and Statistics\nCGPA: 8.9/10\nTECHNOLOGY STACK\nMachine learning libraries: Pytorch, mlflow, NumPy, Pandas, scikit-learn, XGboost, Langchain\nProgramming Languages: Python, SQL, Fortran,LATEX, HTML, CSS\nOthers: FastAPI, Flask, Docker, Docker-Compose, Ansible, AWS(Sagemaker, s3, EC2), Bash, Git, DICOM(Digital\nImaging and Communications in Medicine)\nWORK EXPERIENCE\nAI Consultant- Gateway ventures\nDec 2022 - present\nNLP: RAG/ Autonomous Agents\nBangalore, India\n• Built a RAG + Knowledge graph pipeline with vision transformer models to extract context from video data\nextracted from wearables to serve as a AI personal assistant. Worked with a product manager to align tasks\nand objectives and implement design.\n• Worked closely with external clients for chatbot development: Built and hosted a website for customers to\nleverage OpenAI's API to summarise and answer questions on larger documents. Sped up large document perusal\nfor client by 10x(langchain, fastapi, gpt-4). Further Fine-tuned a custom chatbot based on the client's proprietary\ndata and weblinks, using LLamaIndex for retrieval augmented generation(RAG) to generate a non-hallucinating\nresponse, based on custom corpus of data (tech used: LLamaIndex, gpt4, text embeddings, streamlit).\n• developed an ML pipeline to generate consumer behaviour insight from video data for an ecommerce company\nto improve targetted advertisements for the client.\nMediaire Gmbh\nJul 2022 - Nov 2022\nML engineer/ Customer Support\nBerlin, Germany\nMediaire is a startup building AI products for MRI such as image segmentations and automated diagnostic reports.\nAs part of the early team, was involved in support and data roles\n• as part of the ML team helped fine-tune nnunet for knee and prostate data. Fine tuning involved choice of\nempirical parameters(3D v 2D v 3D cascade for the specific use case), improving eval metric(dice coefficient) by\n7%.\n• Streamlining customer support: creating bug reports, debugging client issues using logs and database queries(sqlite),\ndeveloping structured processes in developing workflows for the customer success team.\n• Tested and secured client connections through a bastion server using Ansible, employing infrastructure as code\nMax Delbruck Center for Molecular Medicine\nSep 2021 - Mar 2022\nResearch Intern\nBerlin, Germany\nMDC is a research institute partnering with industry, dedicated to solving problems in healthcare and biotech- nology\n• Developed data processing pipelines to implement the following: 1. First and Second order phase corrections on\nMRI data. 2. Data cleansing to eliminate background noise thus rendering the highest sharpness of images for\nML pipeline(segmentation, detection etc.)\nSCHOLARSHIPS AND AWARDS\nKVPY Scholarship, awarded by Indian Institute of Science: Undergraduate science scholarship awarded\nwith acceptance rate < 0.5%\n(2014)\nINSPIRE Scholarship for Merit, awarded by Central Board for Secondary Education(CBSE): Awarded\nfor being in the top 0.1% of students in the country at mathematics\n(2015)\n"
                                    },
                                    "meta": {
                                        "name": "test_txt.txt",
                                        "content_type": "text/plain",
                                        "size": 3757,
                                        "collection_name": "file-4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                                    },
                                    "created_at": 1732534506,
                                    "updated_at": 1732534506,
                                },
                                "id": "4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                                "url": "/api/v1/files/4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                                "name": "test_txt.txt",
                                "collection_name": "file-4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                                "status": "uploaded",
                                "size": 3757,
                                "error": "",
                                "itemId": "8c2aed8e-520c-4a8e-ab34-1537cf9d7ce8",
                            }
                        ],
                        "timestamp": 1732534510,
                        "models": ["test"],
                    },
                    {
                        "parentId": "59a20c91-6e3a-4e7f-8e6b-f9bb86454db3",
                        "id": "215657db-7ec7-40b8-bd07-f3c26c769215",
                        "childrenIds": [],
                        "role": "assistant",
                        "content": "{'stream': True, 'model': 'test', 'messages': [{'role': 'system', 'content': '### Task:\\nRespond to the user query using the provided context, incorporating inline citations in the format [source_id] **only when the <source_id> tag is explicitly provided** in the context.\\n\\n### Guidelines:\\n- If you don\\'t know the answer, clearly state that.\\n- If uncertain, ask the user for clarification.\\n- Respond in the same language as the user\\'s query.\\n- If the context is unreadable or of poor quality, inform the user and provide the best possible answer.\\n- If the answer isn\\'t present in the context but you possess the knowledge, explain this to the user and provide the answer using your own understanding.\\n- **Only include inline citations using [source_id] when a <source_id> tag is explicitly provided in the context.**  \\n- Do not cite if the <source_id> tag is not provided in the context.  \\n- Do not use XML tags in your response.\\n- Ensure citations are concise and directly related to the information provided.\\n\\n### Example of Citation:\\nIf the user asks about a specific topic and the information is found in \"whitepaper.pdf\" with a provided <source_id>, the response should include the citation like so:  \\n* \"According to the study, the proposed method increases efficiency by 20% [whitepaper.pdf].\"\\nIf no <source_id> is present, the response should omit the citation.\\n\\n### Output:\\nProvide a clear and direct response to the user\\'s query, including inline citations in the format [source_id] only when the <source_id> tag is present in the context.\\n\\n<context>\\n<source><source_id>test_txt.txt</source_id><source_context>for being in the top 0.1% of students in the country at mathematics\\n(2015)</source_context></source>\\n<source><source_id>test_txt.txt</source_id><source_context>EDUCATION\\nTechnical University, Dortmund\\nJul 2019 - Dec 2020\\nMaster\\'s thesis project on \"Increasing transverse relaxation (T2) in magnetic resonance imaging\"\\nDesigned pulse sequences on Bruker scanners to improve image resolution of MRI images by prolonging the transverse\\nrelaxation by the addition of π refocusing pulses and wrote image processing scripts in MATLAB to create \\'noise\\nmasks\\' to render the MRI image, background noise free\\nIndian Institute for Science Education and Research, Pune\\n2015 - 2020\\nBS-MS dual degree in physics (minor mathematics). Courses included: Statistical mechanics, Non-linear dynamics,\\nLinear algebra, Quantum mechanics, Graph theory, Cryptography, Data Science, Probability and Statistics\\nCGPA: 8.9/10\\nTECHNOLOGY STACK\\nMachine learning libraries: Pytorch, mlflow, NumPy, Pandas, scikit-learn, XGboost, Langchain\\nProgramming Languages: Python, SQL, Fortran,LATEX, HTML, CSS</source_context></source>\\n<source><source_id>test_txt.txt</source_id><source_context>data and weblinks, using LLamaIndex for retrieval augmented generation(RAG) to generate a non-hallucinating\\nresponse, based on custom corpus of data (tech used: LLamaIndex, gpt4, text embeddings, streamlit).\\n• developed an ML pipeline to generate consumer behaviour insight from video data for an ecommerce company\\nto improve targetted advertisements for the client.\\nMediaire Gmbh\\nJul 2022 - Nov 2022\\nML engineer/ Customer Support\\nBerlin, Germany\\nMediaire is a startup building AI products for MRI such as image segmentations and automated diagnostic reports.\\nAs part of the early team, was involved in support and data roles\\n• as part of the ML team helped fine-tune nnunet for knee and prostate data. Fine tuning involved choice of\\nempirical parameters(3D v 2D v 3D cascade for the specific use case), improving eval metric(dice coefficient) by\\n7%.\\n• Streamlining customer support: creating bug reports, debugging client issues using logs and database queries(sqlite),</source_context></source>\\n</context>\\n\\n<user_query>\\nooooo\\n</user_query>\\n'}, {'role': 'user', 'content': 'ooooo'}], 'user': {'name': 'Ashjack', 'id': 'c7ea8c60-03e4-4828-b497-501f94695277', 'email': 'ashrithjacob2@gmail.com', 'role': 'admin'}}",
                        "model": "test",
                        "modelName": "test",
                        "modelIdx": 0,
                        "userContext": None,
                        "timestamp": 1732534510,
                        "sources": [
                            {
                                "source": {
                                    "type": "file",
                                    "file": {
                                        "id": "4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                                        "user_id": "c7ea8c60-03e4-4828-b497-501f94695277",
                                        "hash": "8a2710bb5ee383408d9507f25dc4549c7b8d24aab763ea42caa44898ae7b49ac",
                                        "filename": "test_txt.txt",
                                        "data": {
                                            "content": "EDUCATION\nTechnical University, Dortmund\nJul 2019 - Dec 2020\nMaster's thesis project on \"Increasing transverse relaxation (T2) in magnetic resonance imaging\"\nDesigned pulse sequences on Bruker scanners to improve image resolution of MRI images by prolonging the transverse\nrelaxation by the addition of π refocusing pulses and wrote image processing scripts in MATLAB to create 'noise\nmasks' to render the MRI image, background noise free\nIndian Institute for Science Education and Research, Pune\n2015 - 2020\nBS-MS dual degree in physics (minor mathematics). Courses included: Statistical mechanics, Non-linear dynamics,\nLinear algebra, Quantum mechanics, Graph theory, Cryptography, Data Science, Probability and Statistics\nCGPA: 8.9/10\nTECHNOLOGY STACK\nMachine learning libraries: Pytorch, mlflow, NumPy, Pandas, scikit-learn, XGboost, Langchain\nProgramming Languages: Python, SQL, Fortran,LATEX, HTML, CSS\nOthers: FastAPI, Flask, Docker, Docker-Compose, Ansible, AWS(Sagemaker, s3, EC2), Bash, Git, DICOM(Digital\nImaging and Communications in Medicine)\nWORK EXPERIENCE\nAI Consultant- Gateway ventures\nDec 2022 - present\nNLP: RAG/ Autonomous Agents\nBangalore, India\n• Built a RAG + Knowledge graph pipeline with vision transformer models to extract context from video data\nextracted from wearables to serve as a AI personal assistant. Worked with a product manager to align tasks\nand objectives and implement design.\n• Worked closely with external clients for chatbot development: Built and hosted a website for customers to\nleverage OpenAI's API to summarise and answer questions on larger documents. Sped up large document perusal\nfor client by 10x(langchain, fastapi, gpt-4). Further Fine-tuned a custom chatbot based on the client's proprietary\ndata and weblinks, using LLamaIndex for retrieval augmented generation(RAG) to generate a non-hallucinating\nresponse, based on custom corpus of data (tech used: LLamaIndex, gpt4, text embeddings, streamlit).\n• developed an ML pipeline to generate consumer behaviour insight from video data for an ecommerce company\nto improve targetted advertisements for the client.\nMediaire Gmbh\nJul 2022 - Nov 2022\nML engineer/ Customer Support\nBerlin, Germany\nMediaire is a startup building AI products for MRI such as image segmentations and automated diagnostic reports.\nAs part of the early team, was involved in support and data roles\n• as part of the ML team helped fine-tune nnunet for knee and prostate data. Fine tuning involved choice of\nempirical parameters(3D v 2D v 3D cascade for the specific use case), improving eval metric(dice coefficient) by\n7%.\n• Streamlining customer support: creating bug reports, debugging client issues using logs and database queries(sqlite),\ndeveloping structured processes in developing workflows for the customer success team.\n• Tested and secured client connections through a bastion server using Ansible, employing infrastructure as code\nMax Delbruck Center for Molecular Medicine\nSep 2021 - Mar 2022\nResearch Intern\nBerlin, Germany\nMDC is a research institute partnering with industry, dedicated to solving problems in healthcare and biotech- nology\n• Developed data processing pipelines to implement the following: 1. First and Second order phase corrections on\nMRI data. 2. Data cleansing to eliminate background noise thus rendering the highest sharpness of images for\nML pipeline(segmentation, detection etc.)\nSCHOLARSHIPS AND AWARDS\nKVPY Scholarship, awarded by Indian Institute of Science: Undergraduate science scholarship awarded\nwith acceptance rate < 0.5%\n(2014)\nINSPIRE Scholarship for Merit, awarded by Central Board for Secondary Education(CBSE): Awarded\nfor being in the top 0.1% of students in the country at mathematics\n(2015)\n"
                                        },
                                        "meta": {
                                            "name": "test_txt.txt",
                                            "content_type": "text/plain",
                                            "size": 3757,
                                            "collection_name": "file-4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                                        },
                                        "created_at": 1732534506,
                                        "updated_at": 1732534506,
                                    },
                                    "id": "4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                                    "url": "/api/v1/files/4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                                    "name": "test_txt.txt",
                                    "collection_name": "file-4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                                    "status": "uploaded",
                                    "size": 3757,
                                    "error": "",
                                    "itemId": "8c2aed8e-520c-4a8e-ab34-1537cf9d7ce8",
                                },
                                "document": [
                                    "for being in the top 0.1% of students in the country at mathematics\n(2015)",
                                    "EDUCATION\nTechnical University, Dortmund\nJul 2019 - Dec 2020\nMaster's thesis project on \"Increasing transverse relaxation (T2) in magnetic resonance imaging\"\nDesigned pulse sequences on Bruker scanners to improve image resolution of MRI images by prolonging the transverse\nrelaxation by the addition of π refocusing pulses and wrote image processing scripts in MATLAB to create 'noise\nmasks' to render the MRI image, background noise free\nIndian Institute for Science Education and Research, Pune\n2015 - 2020\nBS-MS dual degree in physics (minor mathematics). Courses included: Statistical mechanics, Non-linear dynamics,\nLinear algebra, Quantum mechanics, Graph theory, Cryptography, Data Science, Probability and Statistics\nCGPA: 8.9/10\nTECHNOLOGY STACK\nMachine learning libraries: Pytorch, mlflow, NumPy, Pandas, scikit-learn, XGboost, Langchain\nProgramming Languages: Python, SQL, Fortran,LATEX, HTML, CSS",
                                    "data and weblinks, using LLamaIndex for retrieval augmented generation(RAG) to generate a non-hallucinating\nresponse, based on custom corpus of data (tech used: LLamaIndex, gpt4, text embeddings, streamlit).\n• developed an ML pipeline to generate consumer behaviour insight from video data for an ecommerce company\nto improve targetted advertisements for the client.\nMediaire Gmbh\nJul 2022 - Nov 2022\nML engineer/ Customer Support\nBerlin, Germany\nMediaire is a startup building AI products for MRI such as image segmentations and automated diagnostic reports.\nAs part of the early team, was involved in support and data roles\n• as part of the ML team helped fine-tune nnunet for knee and prostate data. Fine tuning involved choice of\nempirical parameters(3D v 2D v 3D cascade for the specific use case), improving eval metric(dice coefficient) by\n7%.\n• Streamlining customer support: creating bug reports, debugging client issues using logs and database queries(sqlite),",
                                ],
                                "metadata": [
                                    {
                                        "created_by": "c7ea8c60-03e4-4828-b497-501f94695277",
                                        "embedding_config": '{"engine": "", "model": "sentence-transformers/all-MiniLM-L6-v2"}',
                                        "file_id": "4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                                        "hash": "8a2710bb5ee383408d9507f25dc4549c7b8d24aab763ea42caa44898ae7b49ac",
                                        "name": "test_txt.txt",
                                        "source": "test_txt.txt",
                                        "start_index": 3653,
                                    },
                                    {
                                        "created_by": "c7ea8c60-03e4-4828-b497-501f94695277",
                                        "embedding_config": '{"engine": "", "model": "sentence-transformers/all-MiniLM-L6-v2"}',
                                        "file_id": "4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                                        "hash": "8a2710bb5ee383408d9507f25dc4549c7b8d24aab763ea42caa44898ae7b49ac",
                                        "name": "test_txt.txt",
                                        "source": "test_txt.txt",
                                        "start_index": 0,
                                    },
                                    {
                                        "created_by": "c7ea8c60-03e4-4828-b497-501f94695277",
                                        "embedding_config": '{"engine": "", "model": "sentence-transformers/all-MiniLM-L6-v2"}',
                                        "file_id": "4ca41bd1-52ae-45d3-b98e-f58cacf73be0",
                                        "hash": "8a2710bb5ee383408d9507f25dc4549c7b8d24aab763ea42caa44898ae7b49ac",
                                        "name": "test_txt.txt",
                                        "source": "test_txt.txt",
                                        "start_index": 1751,
                                    },
                                ],
                                "distances": [
                                    0.8640056863409906,
                                    0.908019051016864,
                                    0.9489762110419019,
                                ],
                            }
                        ],
                        "lastSentence": "Courses included: Statistical mechanics, Non-linear dynamics,\\nLinear algebra, Quantum mechanics, Graph theory, Cryptography, Data Science, Probability and Statistics\\nCGPA: 8.9/10\\nTECHNOLOGY STACK\\nMachine learning libraries: Pytorch, mlflow, NumPy, Pandas, scikit-learn, XGboost, Langchain\\nProgramming Languages: Python, SQL, Fortran,LATEX, HTML, CSS</source_context></source>\\n<source><source_id>test_txt.txt</source_id><source_context>data and weblinks, using LLamaIndex for retrieval augmented generation(RAG) to generate a non-hallucinating\\nresponse, based on custom corpus of data (tech used: LLamaIndex, gpt4, text embeddings, streamlit).\\n• developed an ML pipeline to generate consumer behaviour insight from video data for an ecommerce company\\nto improve targetted advertisements for the client.\\nMediaire Gmbh\\nJul 2022 - Nov 2022\\nML engineer/ Customer Support\\nBerlin, Germany\\nMediaire is a startup building AI products for MRI such as image segmentations and automated diagnostic reports.\\nAs part of the early team, was involved in support and data roles\\n• as part of the ML team helped fine-tune nnunet for knee and prostate data.",
                        "done": True,
                    },
                ],
                "chat_id": "447c1e87-6ab1-4622-9f4d-025deec73752",
            },
        },
    },
]
print(len(j))
f1 = j[0]["files"][0]["file"]["data"]["content"]

with open("test_txt.txt", "r") as file:
    f2 = file.read()

print(f1 == f2)
print(f1)

print("-----")
print(f2)

j1 = """
EDUCATION
Technical University, Dortmund
Jul 2019 - Dec 2020
Master's thesis project on "Increasing transverse relaxation (T2) in magnetic resonance imaging"
Designed pulse sequences on Bruker scanners to improve image resolution of MRI images by prolonging the transverse
relaxation by the addition of π refocusing pulses and wrote image processing scripts in MATLAB to create 'noise
masks' to render the MRI image, background noise free
Indian Institute for Science Education and Research, Pune
2015 - 2020
BS-MS dual degree in physics (minor mathematics). Courses included: Statistical mechanics, Non-linear dynamics,
Linear algebra, Quantum mechanics, Graph theory, Cryptography, Data Science, Probability and Statistics
CGPA: 8.9/10
TECHNOLOGY STACK
Machine learning libraries: Pytorch, mlflow, NumPy, Pandas, scikit-learn, XGboost, Langchain
Programming Languages: Python, SQL, Fortran,LATEX, HTML, CSS
Others: FastAPI, Flask, Docker, Docker-Compose, Ansible, AWS(Sagemaker, s3, EC2), Bash, Git, DICOM(Digital
Imaging and Communications in Medicine)
WORK EXPERIENCE
AI Consultant- Gateway ventures
Dec 2022 - present
NLP: RAG/ Autonomous Agents
Bangalore, India
• Built a RAG + Knowledge graph pipeline with vision transformer models to extract context from video data
extracted from wearables to serve as a AI personal assistant. Worked with a product manager to align tasks
and objectives and implement design.
• Worked closely with external clients for chatbot development: Built and hosted a website for customers to
leverage OpenAI's API to summarise and answer questions on larger documents. Sped up large document perusal
for client by 10x(langchain, fastapi, gpt-4). Further Fine-tuned a custom chatbot based on the client's proprietary
data and weblinks, using LLamaIndex for retrieval augmented generation(RAG) to generate a non-hallucinating
response, based on custom corpus of data (tech used: LLamaIndex, gpt4, text embeddings, streamlit).
• developed an ML pipeline to generate consumer behaviour insight from video data for an ecommerce company
to improve targetted advertisements for the client.
Mediaire Gmbh
Jul 2022 - Nov 2022
ML engineer/ Customer Support
Berlin, Germany
Mediaire is a startup building AI products for MRI such as image segmentations and automated diagnostic reports.
As part of the early team, was involved in support and data roles
• as part of the ML team helped fine-tune nnunet for knee and prostate data. Fine tuning involved choice of
empirical parameters(3D v 2D v 3D cascade for the specific use case), improving eval metric(dice coefficient) by
7%.
• Streamlining customer support: creating bug reports, debugging client issues using logs and database queries(sqlite),
developing structured processes in developing workflows for the customer success team.
• Tested and secured client connections through a bastion server using Ansible, employing infrastructure as code
Max Delbruck Center for Molecular Medicine
Sep 2021 - Mar 2022
Research Intern
Berlin, Germany
MDC is a research institute partnering with industry, dedicated to solving problems in healthcare and biotech- nology
• Developed data processing pipelines to implement the following: 1. First and Second order phase corrections on
MRI data. 2. Data cleansing to eliminate background noise thus rendering the highest sharpness of images for
ML pipeline(segmentation, detection etc.)
SCHOLARSHIPS AND AWARDS
KVPY Scholarship, awarded by Indian Institute of Science: Undergraduate science scholarship awarded
with acceptance rate < 0.5%
(2014)
INSPIRE Scholarship for Merit, awarded by Central Board for Secondary Education(CBSE): Awarded
for being in the top 0.1% of students in the country at mathematics
(2015)
"""

j2 = """
EDUCATION
Technical University, Dortmund
Jul 2019 - Dec 2020
Master’s thesis project on “Increasing transverse relaxation (T2) in magnetic resonance imaging”
Designed pulse sequences on Bruker scanners to improve image resolution of MRI images by prolonging the transverse
relaxation by the addition of π refocusing pulses and wrote image processing scripts in MATLAB to create ’noise
masks’ to render the MRI image, background noise free
Indian Institute for Science Education and Research, Pune
2015 - 2020
BS-MS dual degree in physics (minor mathematics). Courses included: Statistical mechanics, Non-linear dynamics,
Linear algebra, Quantum mechanics, Graph theory, Cryptography, Data Science, Probability and Statistics
CGPA: 8.9/10
TECHNOLOGY STACK
Machine learning libraries: Pytorch, mlflow, NumPy, Pandas, scikit-learn, XGboost, Langchain
Programming Languages: Python, SQL, Fortran,LATEX, HTML, CSS
Others: FastAPI, Flask, Docker, Docker-Compose, Ansible, AWS(Sagemaker, s3, EC2), Bash, Git, DICOM(Digital
Imaging and Communications in Medicine)
WORK EXPERIENCE
AI Consultant- Gateway ventures
Dec 2022 - present
NLP: RAG/ Autonomous Agents
Bangalore, India
• Built a RAG + Knowledge graph pipeline with vision transformer models to extract context from video data
extracted from wearables to serve as a AI personal assistant. Worked with a product manager to align tasks
and objectives and implement design.
• Worked closely with external clients for chatbot development: Built and hosted a website for customers to
leverage OpenAI’s API to summarise and answer questions on larger documents. Sped up large document perusal
for client by 10x(langchain, fastapi, gpt-4). Further Fine-tuned a custom chatbot based on the client’s proprietary
data and weblinks, using LLamaIndex for retrieval augmented generation(RAG) to generate a non-hallucinating
response, based on custom corpus of data (tech used: LLamaIndex, gpt4, text embeddings, streamlit).
• developed an ML pipeline to generate consumer behaviour insight from video data for an ecommerce company
to improve targetted advertisements for the client.
Mediaire Gmbh
Jul 2022 - Nov 2022
ML engineer/ Customer Support
Berlin, Germany
Mediaire is a startup building AI products for MRI such as image segmentations and automated diagnostic reports.
As part of the early team, was involved in support and data roles
• as part of the ML team helped fine-tune nnunet for knee and prostate data. Fine tuning involved choice of
empirical parameters(3D v 2D v 3D cascade for the specific use case), improving eval metric(dice coefficient) by
7%.
• Streamlining customer support: creating bug reports, debugging client issues using logs and database queries(sqlite),
developing structured processes in developing workflows for the customer success team.
• Tested and secured client connections through a bastion server using Ansible, employing infrastructure as code
Max Delbruck Center for Molecular Medicine
Sep 2021 - Mar 2022
Research Intern
Berlin, Germany
MDC is a research institute partnering with industry, dedicated to solving problems in healthcare and biotech- nology
• Developed data processing pipelines to implement the following: 1. First and Second order phase corrections on
MRI data. 2. Data cleansing to eliminate background noise thus rendering the highest sharpness of images for
ML pipeline(segmentation, detection etc.)
SCHOLARSHIPS AND AWARDS
KVPY Scholarship, awarded by Indian Institute of Science: Undergraduate science scholarship awarded
with acceptance rate < 0.5%
(2014)
INSPIRE Scholarship for Merit, awarded by Central Board for Secondary Education(CBSE): Awarded
for being in the top 0.1% of students in the country at mathematics
(2015)
"""
print(j1 == j2)

def diff(s1,s2):
    d = [i for i in range(len(s1)) if s1[i] != s2[i]]
    for i in d:
        print(i, s1[i], s2[i])

diff(j1,j2)
