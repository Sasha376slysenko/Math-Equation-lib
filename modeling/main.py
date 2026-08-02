from general_analysis import GeneralAnalysis
from plot_graphs import PlotGraphs
from model import ModelTelemetry

def main() -> None:
    telemetry = ModelTelemetry()
    telemetry.run_model()

    plot_graphs = PlotGraphs()
    plot_graphs.forward_analysis()

    total_analysis = GeneralAnalysis()
    total_analysis.forward_analysis()


if __name__ == "__main__":
    main()
