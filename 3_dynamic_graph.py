import dash
from dash.dependencies import Input,Output
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web
import datetime


app = dash.Dash()

app.layout = html.Div(children=[
    html.Div('symbol to graph'),
    dcc.Input(id='input',value='',type='text'),
    html.Div(id='output-graph')
    ])

@app.callback(
    Output(component_id='output-graph',component_property='children'),
    [Input(component_id='input',component_property='value')]
    )
def update_graph(input_data):
        start = datetime.datetime(2015,1,1)
        end = datetime.datetime.now()
        df=web.DataReader(input_data.upper(),'quandl',start,end)
        return dcc.Graph(
			id='example',
			figure={
				'data':[
					{'x':df.index,'y':df.Open,'type':'line','name':'Open'},
					{'x':df.index,'y':df.Close,'type':'line','name':'Close'}
				],
				'layout':{
					'title':input_data.upper()
				}
			}
		)
		
if __name__=='__main__':
    app.run_server(debug=True)