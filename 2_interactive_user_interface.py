##################################################################
##											 In this tutorial:											##
##																															##
##		How we can have the user interact with the app itself.		##
##		Pull the information and do something with it.						##
##		Update the app live in realtime.													##
##################################################################

import dash
from dash.dependencies import Input,Output
import dash_core_components as dcc
import dash_html_components as html

#Start the application

app = dash.Dash()

app.layout = html.Div(children=[
	# Input from dash_core_components
	# Id is required in order to interact with it, if we want to populate it or apply somme rulels to it
	dcc.Input(id='input',value='Enter Something',type='text'),
	html.Div(id='output')
	])
	
# Function to handle the input.
@app.callback(
	Output(component_id='output',component_property='children'),
	[Input(component_id='input',component_property='value')]
	)
def update_value(input_data):
	return "Input:{}".format(input_data)
	'''try:
		return str(float(input_data)**2)
	except:
		return "Some Error occurred"'''

if __name__=='__main__':
	app.run_server(debug=True)