import { Graphviz } from "@hpcc-js/wasm-graphviz";
import { addData } from "./add-data.js";
import data from "../data.js";

async function getSVG() {
    const graphviz = await Graphviz.load();

    using graph = graphviz.createGraph();
    addData(graph, data);
    console.log(graph.toDot());
    return graph.layout(undefined, "dot");
}

export default await getSVG();
