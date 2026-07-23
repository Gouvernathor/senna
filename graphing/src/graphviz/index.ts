import { Graphviz } from "@hpcc-js/wasm-graphviz";
import { addData } from "./add-data.js";
import data from "../data.js";

async function getSVG() {
    const graphviz = await Graphviz.load();

    using graph = graphviz.createGraph();
    addData(graph, data);
    return graph.layout();
}

export default await getSVG();
