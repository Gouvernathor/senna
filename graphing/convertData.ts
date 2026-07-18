import { ElementsDefinition } from "cytoscape";
import { DataRoot } from "./data.js";

export function convertData(data: DataRoot): ElementsDefinition {
    return {
        nodes: Object.keys(data.situations).map(id => ({ id, data: data.situations[id] })),
        edges: data["événements"].flatMap(({ n, name, desc, variantes, optional }) => {
            const data = { name, desc };
            return variantes.flatMap(({ id, situations = [], condition, "résultat": resultat, nomination }) => {
                return situations.map(situation => ({
                    data: {
                        id: id ? `${n}-${id}` : `${n}`,
                        source: situation,
                        target: resultat,

                        // nothing is done with this yet
                        condition,
                        nomination,
                        ...data,
                        optional,
                    },
                }));
            });
        }),
    };
}
