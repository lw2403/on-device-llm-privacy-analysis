# Privacy-first On-Device LLMs

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

--- 

# Analysis 

* I'll record the answers and score each question in a big .csv file
* I'll do some analysis of each test with pandas, matplotlib etc...

---

# My Own Pruning (Future Consideration)

* I'm using a pre-pruned 7B model created by TII
* I'm using GPT4ALL to run inference on my laptop
* I could get access to an A100 or better GPU from Brown and prune and train my own model with Pytorch or Tensorflow
* I could also write my own inference code for these models, to better guarantee privacy because while GPT4ALL is open source it could theoretically still be sending my private info to the UAE or something 