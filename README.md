# Privacy-first On-Device LLMs Presentation

Possibilites and challenges

---

# The problem

* LLMs are great BUT
* They require specialized hardware to run (Big GPUs, $40,000 servers)
* Most popular services are therefore ran in the cloud (ChatGPT, Claude, Bard, Huggingface Chat etc...)
* In order to use them for sensitive topics, you need to consent to giving "Big Tech" your personal information.

---

# A solution? On-Device LLMs

* On-device LLMs are possible, but are much smaller than cloud/enterprize options
* for example GPT-3.5 has 175 billion parameters (it tracks that many "relationships" in text via its neural network) but most models you can run on your laptop have only 7 billion parameters (sometimes 13 if you have a fancy and expensive gaming laptop)

---

# LLM Leaderboard
* Compares open-source models of varying parameter counts 7-180 billion and beyond
* Uses standard tests and compares their scores (ARC, HellaSwag, MMLU etc..)
<img width="903" alt="Screenshot 2023-11-30 at 1 49 15 PM" src="https://github.com/lw2403/on-device-llm-privacy-analysis/assets/46736926/48495082-d308-4502-b2a5-02184b3a711b">

https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard

---

# My Testing Setup
* Compare [Falcon 180B](https://huggingface.co/tiiuae/falcon-180B) (one of the most sophisticated open-source LLMs, comparable to GPT-3.5 but a little worse than GPT-4) available with GPU inference on [HuggingFace Chat](https://huggingface.co/chat/) to
* [Falcon 7B](https://huggingface.co/tiiuae/falcon-7b) available for offline, privacy friendly local chat on my laptop via [GPT4ALL](https://gpt4all.io/index.html)

---

# Testing 

* I'm going to give each model 100 questions across the following categories:
    1. **Personal Questions**
    2. **Common Helper Questions**
    3. **Logical Reasoning Questions**
    4. **Text Completion and Comprehnsion**
    5. **Programming and Code Generation**
    6. **Creative Writing and Storytelling**
    7. **Translation and Language Proficiency**
    8. **Current Events and Information Retrieval**
    9. **Mathematical Problem Solving**
    10. **Philosophical and Ethical Questions**

* Bad Example 1: Math
  <img width="905" alt="Screenshot 2023-11-30 at 1 53 42 PM" src="https://github.com/lw2403/on-device-llm-privacy-analysis/assets/46736926/aaee3892-8424-434c-b250-56f48af0bd87">
  <img width="474" alt="Screenshot 2023-11-30 at 1 54 35 PM" src="https://github.com/lw2403/on-device-llm-privacy-analysis/assets/46736926/a160135e-d882-4a34-b352-36498ca39d83">


* Bad Example 2: Logical
  <img width="1046" alt="Screenshot 2023-11-30 at 1 56 12 PM" src="https://github.com/lw2403/on-device-llm-privacy-analysis/assets/46736926/342167e9-2940-46ad-bc76-48fe485b793f">
  <img width="412" alt="Screenshot 2023-11-30 at 1 55 49 PM" src="https://github.com/lw2403/on-device-llm-privacy-analysis/assets/46736926/d0680c7b-e9eb-4a61-87b0-cfe0c976b9f6">

* Bad Example 3: Logical
  <img width="1182" alt="Screenshot 2023-11-30 at 1 57 15 PM" src="https://github.com/lw2403/on-device-llm-privacy-analysis/assets/46736926/b5f7117b-e004-4aaa-9dd4-e1d05a305b82">
  <img width="864" alt="Screenshot 2023-11-30 at 1 57 01 PM" src="https://github.com/lw2403/on-device-llm-privacy-analysis/assets/46736926/16730dc1-04ae-4ddc-a256-dc9bb84f2425">

* Similar Example 1: Sentence Completion
  <img width="610" alt="Screenshot 2023-11-30 at 2 00 28 PM" src="https://github.com/lw2403/on-device-llm-privacy-analysis/assets/46736926/bac86ca0-155f-4f99-9d61-0a4435892e4e">
  <img width="674" alt="Screenshot 2023-11-30 at 2 01 14 PM" src="https://github.com/lw2403/on-device-llm-privacy-analysis/assets/46736926/00c142ed-bfb9-4069-a7fe-bd7934c4440a">

* Similar Example 2: Helper
  <img width="1101" alt="Screenshot 2023-11-30 at 2 23 56 PM" src="https://github.com/lw2403/on-device-llm-privacy-analysis/assets/46736926/9f788cae-9148-408f-aa5b-ebde2e228458">
 <img width="690" alt="Screenshot 2023-11-30 at 2 24 43 PM" src="https://github.com/lw2403/on-device-llm-privacy-analysis/assets/46736926/4851dbd7-8e69-4963-92c6-aeaaaa288acf">


--- 

# Analysis 

* I've record the answers and score each question in a big .csv file
* I've done analysis of each test with pandas, matplotlib etc to assess the accuracy, helpfulness, length, word clouds etc. 

---

# My Own Pruning (Consideration)

* I'm using a pre-pruned 7B model created by TII
* I'm using GPT4ALL to run inference on my laptop
* I could get access to an A100 or better GPU and prune and train my own model with Pytorch or Tensorflow
* I could also write my own inference code for these models, to better guarantee privacy because while GPT4ALL is open source it could theoretically still be sending my private info to the UAE or something 
