import plotly.express as px

from dash import Dash, dcc, html
from src.data import get_closing_prices

# Petrobras Market Share
data = get_closing_prices(tickers="PBR", period="1mo")

app = Dash(__name__)

fig = px.line(data, x=data.index, y="close", title="Closed Market Share (PBR - 1mo)")

app.layout = html.Div(
    [
        html.H1(
            children="Demo Cloud Run App - GitHub: @brenoAV",
            style={"textAlign": "center"},
        ),
        dcc.Graph(figure=fig, id="graphic-content"),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=False, host="0.0.0.0", port=8080)
