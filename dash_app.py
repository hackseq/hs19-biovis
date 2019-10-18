import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import igraph


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Link", href="#")),
        dbc.DropdownMenu(
            nav=True,
            in_navbar=True,
            label="Menu",
            children=[
                dbc.DropdownMenuItem("Entry 1"),
                dbc.DropdownMenuItem("Entry 2"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Entry 3"),
            ],
        ),
    ],
    brand="RefSeq Genome Browser",
    brand_href="#",
    sticky="top",
)

cluster_buttons = dbc.FormGroup(
    [
        dbc.Label("Clustering Method"),
        dbc.RadioItems(
            options=[
                {"label": "Connectivity", "value": "connectivity"},
                {"label": "Option 2", "value": 2},
                {"label": "Disabled option", "value": 3, "disabled": True},
            ],
            value=1,
            id="radioitems-input",
        ),
    ]
)

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H3("Filter"),
                        html.Br(),
                        dbc.Input(id="input", placeholder="Find a genome...", type="text"),
                        html.Br(),
                        cluster_buttons
                    ],
                    width=2
                ),
                dbc.Col(
                    [
                        html.H3("Network Explorer"),
                        dcc.Graph(
                            figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}
                        ),
                    ],
                    width=7
                ),
                dbc.Col([html.H3("Graph Details")],
                width=3)
            ]
        )
    ],
    className="mt-4",
)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([navbar, body])

if __name__ == "__main__":
    app.run_server()