import dash
import dash_core_components as dcc
import dash_table
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from ceramic.graphlib import map_graph

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
df = pd.read_csv('ceramic/sample_data/by_month_cluster_200.csv')

app.layout = html.Div([

    html.Div([
        html.H1(children='MyCaterPillars'),
        html.Div(children='''
        A dashboard for fleet fuel management and optimization!
        '''),
    ]),

    html.Div([
        dcc.Graph(
            id='map-graph',
            figure=map_graph(df)
        ),

        dash_table.DataTable(
            id='output-table',
            columns=[{"name": i, "id": i} for i in df.columns],
        )

    ]),
])


def get_filtered_data(indices: list):
    return df.loc[indices].to_dict('records')


@app.callback(
    Output('output-table', 'data'),
    Input('map-graph', 'selectedData'))
def update_table(selectedData):
    indices_to_show = []
    for i in range(len(selectedData['points'])):
        # print(hoverData['points'][i])
        # print("\n")
        indices_to_show.append(selectedData['points'][i]['pointNumber'])
    print(indices_to_show)
    return get_filtered_data(indices_to_show)


# @app.callback(Output('output_table', 'data'),
#             Input('submit-marge', 'n_clicks'),
#             #Input('produkt_daten', 'data'),
#             State('input_marge', 'value'))
# #berechnen des output tables
# def rows_berechnen(n_clicks, marge):
#     if n_clicks >0 :
#         df_preise = pd.DataFrame(columns = {'Produkt', 'Ebay', 'Amazon', 'Real', 'Webshop'})
#         test = {'Produkt' : 'marge', 'Ebay': marge, 'Amazon': marge, 'Real': marge, 'Webshop': marge}
#         test2 = {'Produkt' : 'marge', 'Ebay': marge, 'Amazon': marge, 'Real': marge, 'Webshop': marge}
#         df_preise = df_preise.append(test, ignore_index=True)
#         df_preise = df_preise.append(test2, ignore_index=True)
#
#         print(df_preise)
#         df = df_preise.to_dict(orient ='records')
#         return df
#     raise PreventUpdate

if __name__ == '__main__':
    app.run_server(debug=True)