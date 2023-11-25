# Tailing

As a large language model dedicated to judicial institutions and law enforcement personnel, "TaiLing" aims to facilitate more accurate evidence analysis and case understanding in the field of justice, providing professional and precise intelligent assistance for judicial proceedings. It offers a diverse range of judicial services, including text verification, information extraction, sentencing assistance, judicial exam support, and human-computer dialogue. This showcases the extensive applications of large language models in the judicial domain and their immense potential in enhancing work efficiency and accuracy.

Core Capabilities of “TaiLing”
1.	Text Verification: The text verification task is dedicated to automatically detecting and correcting grammar, spelling, and factual errors in judicial documents. Its key focus is on improving document quality, reducing human errors, and thereby ensuring the reliability of legal documents. For legal professionals, this means saving a significant amount of time in proofreading and corrections, ensuring adherence to professional standards for documents. 
2.	Information Extraction: The information extraction task focuses on accurately extracting key information from complex judicial documents, such as individuals, locations, events, and their interrelationships. It rapidly identifies and categorizes crucial data points to support case analysis and the formulation of legal decisions. This efficient information extraction capability enables legal professionals to quickly grasp the overall context of a case, facilitating more accurate evidence analysis and case understanding.
3.	Sentencing Assistance: The sentencing assistance task aims to provide judicial professionals with sentencing recommendations based on data and historical cases to enhance the objectivity and consistency of judgments. This task focuses on analyzing sentencing standards for similar cases, considering case-specific factors such as the nature of the offense and the defendant's background. By constructing predictive models, it generates reasonable sentencing references.

Base Model
The TaiLing pedestal model adopts Alibaba Cloud's Qwen-7B series, which boasts 70 billion parameters. After pre-training on a massive dataset of over 2 trillion tokens, it demonstrates excellent performance in text comprehension and generation, pattern recognition, decision support, and other aspects. During the model training process, we utilized 8 Nvidia A40 48 GB graphics cards and integrated QLoRA technology to customize and fine-tune the pedestal model specifically for the judicial domain. Our training code is optimized based on the Firefly project to ensure higher efficiency and stability in the model's performance.

Data Resources
•	moss-003-sft-data : https://huggingface.co/datasets/YeungNLP/moss-003-sft-data
•	firefly-train-1.1M : https://huggingface.co/datasets/YeungNLP/firefly-train-1.1M
•	conversation data: We have compiled a portion of conversation datasets, including approximately 60,000 entries. The download link will be provided shortly.
•	judgment prediction: https://cail.oss-cn-qingdao.aliyuncs.com/CAIL2018_ALL_DATA.zip 
•	Information Extraction: https://huggingface.co/datasets/cail2018,https://github.com/china-ai-law-challenge/CAIL2022
•	Event Detection: https://github.com/thunlp/LEVEN,https://github.com/china-ai-law-challenge/CAIL2022
•	Judicial exam: https://jecqa.thunlp.org/
•	Text Checking: The dataset can be downloaded from "./data"
•	Summary Generation: We have compiled a portion of summary datasets, including approximately 60,000 entries. The download link will be provided shortly

How To Start With "TaiLing"
Before you begin, ensure that you have configured the environment and installed the relevant code packages. 
pip install -r requirements.txt

How To Inference
If you wish to use "TaiLing" for inference, you can run “python chat.py”. 








