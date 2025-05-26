from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain

import os
from secret_key import gemini_secretKey
os.environ['GOOGLE_API_KEY'] = gemini_secretKey

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=gemini_secretKey, temperature= 0.7)

def generate_restaurant_name_menu(cuisine):

    # first prompt / Chain 1 
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a {cuisine} restaurant. Suggest only one great name for it.")

    name_chain = LLMChain(
        llm=llm,
        prompt=prompt_template_name,
        output_key='restaurant_name'  # This will be used as input for the next chain
        )

    # second prompt / Chain 2
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest me some food menu items for {restaurant_name} Return it as a comma separated list.")

    food_item_chain = LLMChain(
        llm=llm,
        prompt=prompt_template_items , # This will take the output from the first chain
        output_key = 'menu_items')
    
    from langchain.chains import SequentialChain

    sequential_chain = SequentialChain(chains=[name_chain, food_item_chain],
                    input_variables=['cuisine'], output_variables=['restaurant_name', 'menu_items'])
    
    response = sequential_chain.invoke({"cuisine": cuisine})
    return response


if __name__ == "__main__":
    print(generate_restaurant_name_menu("Indian"))