from setuptools import find_packages, setup

setup(
   name = 'medicalchatbot',
   version= '0.0.1',
   author= 'Merlyn',
   author_email= 'omagwamerlyn@gmail.com',
   install_requires = ["ctransformers==0.2.5", "sentence-transformers==2.2.2", "pinecone-client==2.2.4", "langchain==0.0.225", "flask", "pypdf", "python-dotenv"],
   packages= find_packages()

)