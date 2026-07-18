import cytoscape from "cytoscape";
import data from "./data.js";
import { convertData, styleOptions } from "./convertData.js";

cytoscape({
    elements: convertData(data),
    style: styleOptions,
});
