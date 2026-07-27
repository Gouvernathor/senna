import { ElementsDefinition, StylesheetJson } from "cytoscape";
import { DataRoot } from "../data.js";

export function convertData(data: DataRoot): ElementsDefinition {
    return {
        nodes: Object.keys(data.situations).map(id => ({ data: { id, ...data.situations[id]! } })),
        edges: data["événements"].flatMap(({ n, name, desc, variantes, optional }) => {
            return variantes.flatMap(({ id, name: varianteName, situations = [], condition, "résultat": resultat, nomination }) => {
                const classes: string[] = [];
                if (optional) {
                    classes.push("optional");
                } else if (nomination) {
                    classes.push("nomination");
                }
                return situations.map(situation => ({
                    data: {
                        id: id ? `${n}-${id}` : `${n}`,
                        source: situation,
                        target: resultat,

                        name: varianteName ?? name,
                        nomination,
                        optional,
                        // nothing is done with these yet
                        condition,
                        desc,
                    },
                    classes,
                }));
            });
        }),
    };
}

export const styleOptions: StylesheetJson = [{
    selector: "edge",
    style: {
        "target-arrow-shape": "triangle",
        "curve-style": "bezier",
        "control-point-step-size": 100,
        // "control-point-weight": .7,
        "text-rotation": "autorotate",
        // "text-margin-y": -16,
    },
}, {
    selector: "node[name]",
    style: {
        label: "data(name)",
    },
}, {
    selector: "node:parent",
    style: {
        shape: "round-rectangle",
        // "text-valign": "top-inside",
    },
}, {
    selector: "node:childless",
    style: {
        shape: "ellipse",
        width: "label",
        padding: "20px",
        "text-valign": "center",
        "text-halign": "center",
    },
}, {
    selector: "edge[name]",
    style: {
        label: "data(name)",
    },
}, {
    selector: ".nomination",
    style: {
        color: "darkslateblue",
        "line-color": "blue",
        "target-arrow-color": "blue",
    },
}, {
    selector: ".optional",
    style: {
        color: "orangered",
        "line-color": "orange",
        "target-arrow-color": "orange",
    },
}];
