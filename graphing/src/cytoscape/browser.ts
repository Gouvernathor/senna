import cytoscape from "cytoscape";
import data from "../data.js";
import { convertData, styleOptions } from "./convert-data.js";

cytoscape({
    container: document.getElementById("cy"),
    elements: convertData(data),
    style: styleOptions,
    layout: {
        name: "grid",
        nodeDimensionsIncludeLabels: true,
    },
});
