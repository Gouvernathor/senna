import { ElementsDefinition, StylesheetJson } from "cytoscape";
import { DataRoot } from "./data.js";

export function convertData(data: DataRoot): ElementsDefinition {
    return {
        nodes: Object.keys(data.situations).map(id => ({ id, data: data.situations[id] })),
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

export const styleOptions: StylesheetJson = [
    {
        selector: "[name]",
        style: {
            label: "data(name)",
        },
    }
];
