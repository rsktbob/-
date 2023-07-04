import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

major_disciplines_annual_change = {
    '機械工程系': [598, 584, 580, 583, 521, 467],
    '電機工程系': [538, 517, 521, 537, 556, 557],
    '化學工程與生物科技系': [509, 498, 512, 521, 529, 553],
    '土木工程系': [419, 442, 460, 481, 464, 459],
    '電子工程系': [390, 393, 400, 417, 419, 437],
    '材料及資源工程系': [376, 380, 390, 412, 418, 417],
    '工業工程與管理系': [320, 324, 332, 328, 313, 338],
    '工業設計系': [277, 255, 282, 278, 263, 285],
    '互動設計系': [265, 288, 312, 307, 305, 300],
    '經營管理系': [234, 257, 272, 265, 247, 245]}

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='北科大十大科系學生數變化'),

    dcc.Dropdown(
        id='subject-dropdown',
        options=[
            {'label': '全部科系', 'value': '全部'}
        ] + [{'label': subject, 'value': subject} for subject in major_disciplines_annual_change],
        value='全部'
    ),

    dcc.Graph(id='major-disciplines-graph')
])


@app.callback(
    Output('major-disciplines-graph', 'figure'),
    Input('subject-dropdown', 'value')
)
def update_figure(subject):
    if subject == '全部':
        traces = [{'x': [106, 107, 108, 109, 110, 111], 'y': major_disciplines_annual_change[subject], 'name': subject}
                  for subject in major_disciplines_annual_change]
    else:
        traces = [{'x': [106, 107, 108, 109, 110, 111],
                   'y': major_disciplines_annual_change[subject], 'name': subject}]

    return {
        'data': traces,
        'layout': {
            'title': f'{subject} 學生數變化',
            'xaxis': {'title': '學年度'},
            'yaxis': {'title': '學生數'}
        }
    }


if __name__ == '__main__':
    app.run_server(debug=True)
