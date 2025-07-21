from setuptools import find_packages, setup

setup(
   name = 'medicalchatbot',
   version= '0.0.1',
   author= 'Merlyn',
   author_email= 'omagwamerlyn@gmail.com',
   install_requires = ["ctransformers", "sentence-transformers", "pinecone-client", "langchain", "langchain-community","flask", "pypdf", "python-dotenv"],
   packages= find_packages()

)