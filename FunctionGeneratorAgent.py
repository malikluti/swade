from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
#from langchain.agents.agent_toolkits import create_csv_agent
import os
import validators
import pandas as pd
from rdflib import Graph
import rdflib
import parser

{'name': 'Pipe', 'comment': 'A pipe is a passage of water flowing in a closed conduit (i.e., not subject to atmospheric pressure).', 'label': 'Pipe', 'properties': ['JointMaterial', 'Lining', 'hasMaterial', 'hasCathodic', 'hasDiameter', 'InstallationDate', 'JointType', 'Length', 'Type']}
{'name': 'City', 'comment': 'A city is a large human settlement. A city is distinguished from other human settlements by its relatively great size, but also by its functions and its special symbolic status, which may be conferred by a central authority. (https://en.wikipedia.org/wiki/City)', 'label': 'City', 'parents': ['AdministrativeArea'], 'subClasses': [], 'individuals': [], 'properties': []}


base_filepath = "/Users/malikluti/Documents/MyProjects/SWADE/SWADE_Project/Data_Samples"
city_a_csv = os.path.join(base_filepath, 'city_A.csv')
city_b_csv = os.path.join(base_filepath, 'city_B.csv')

city_a_content = pd.read_csv(city_a_csv)
#print(city_a_content.iloc[0])

def get_column_names(pandas_input):
    return pandas_input.columns.tolist()

city_a_column_names = get_column_names(city_a_content)
#print(city_a_content.iloc[0].tolist())

city_a_json = []

for row_index in range(city_a_content.shape[0]):
    current_row = []

    for index, raw_item in enumerate(city_a_content.iloc[row_index].tolist()):
        current_row_json = {
            "original_column_name": None,
            "original_item_value": None,
            "ontology_class_name": None,
            "ontology_instance_value": None
        }
        current_row_json["original_column_name"] = city_a_column_names[index]
        current_row_json["original_item_value"] = raw_item

        current_row.append(current_row_json)

    city_a_json.append(current_row)

#print(city_a_json)
0 # LLM ESTIMATING THE CLASS STARTING FROM THE CSV COLUMN NAMES AND AN ONTHOLOGY CLASSES DESCRIPTION
1 # LLM FINDING THE MATCH BETWEEN THE CLASSES AND THE ORIGINAL CSV NAMES
2 # SET THE NAME OF THE GRAPH CLASSES TO THE JSON OBJECT (ontology_class_name)
3 # LLM GENERATE A PYTHON FUNCTION PER CLASS THAT TURNS THE DATA FROM THE original_item_value format to ontology_instance_value format
4 # LLM GENERTAE THE EXPECTED OUTPUT FROM 5 ROWS
5 # TEST THE FUNCTION GENERATED BY STEP 3 WITH THE TEST SET GENERATED BY STEP 4
6 # ITERATE STEPS 3, 4, 5 FOR EVERY COLUMN IN THE ORIGINAL CSV/JSON FILE
7 # EXECUTE THE PYTHON FUNCTIONS OVER EVERY ROW OF THE JSON OBJECT

"""
funct 1 - col 1
funct 2 - col 2
"""
"" \
"def turn_date_into_ontology_date(date):" \
#"" datetime dateimt\
#    reutnr ontology_instance_value
""

"""
original_item_value: '63
ontology_instance_value: 1963
"""


"""
agent = create_csv_agent(
    ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613", ),
    city_a,
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
)

agent.run("how many rows are there in the file?")
"""

# new code
swade = NameSpace("http://www.semanticweb.org/malikluti/ontologies/swade")
query = prepareQuery("""
	SELECT ?code 
	where
	{
   		?x a swade:Material .
   		?x swade:code ?code .
	}
	""", initNs={'swade': swade})

# Execute the query
results = gx.query(query)
print(results)
# Print the results
for res in results:
    print(f"{res['material']}")
    if df['material'] == res['material']:
        ! pip
        install
        rdflib
        ! pip
        install
        rdflib - jsonld
        !
        ! pip
        install
        pydotplus
        ! pip
        install
        graphviz