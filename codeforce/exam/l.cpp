#include <iostream>
#include <vector>
using namespace std;

long maxFlow = 0, totalSourceValence = 0, totalSinkValence = 0;

class Edge {
public:
    int from, to, capacity;

    Edge(int _from = -1, int _to = -1, int _capacity = 0)
        : from(_from), to(_to), capacity(_capacity) {}
};

class Graph {
public:
    int height, width, numVertices;
    vector<vector<Edge> > edges;
    vector<bool> visited;

    Graph(int _height, int _width);

    void addEdge(int from, int to, int capacity);
    void initializeGraph();
    void resetVisited();
    int vertexID(int i, int j);
};

Graph::Graph(int _height, int _width)
    : height(_height), width(_width) {
    numVertices = height * width + 2;
    edges.resize(numVertices);
    visited.resize(numVertices, false);
}

void Graph::addEdge(int from, int to, int capacity) {
    edges[from].emplace_back(from, to, capacity);
    edges[to].emplace_back(to, from, 0); // Обратное ребро с 0 пропускной способностью
}

void Graph::resetVisited() {
    fill(visited.begin(), visited.end(), false);
}

int Graph::vertexID(int i, int j) {
    return i * width + j + 1;
}

int findReverseEdgeIndex(const Graph& graph, const Edge& edge) {
    for (size_t i = 0; i < graph.edges[edge.to].size(); ++i) {
        if (graph.edges[edge.to][i].to == edge.from) {
            return i;
        }
    }
    return -1;
}

int atomValence(char atom) {
    switch (atom) {
        case 'H': return 1;
        case 'O': return 2;
        case 'N': return 3;
        case 'C': return 4;
        default: return 0;
    }
}

void Graph::initializeGraph() {
    for (int i = 0; i < height; ++i) {
        for (int j = 0; j < width; ++j) {
            char atom;
            cin >> atom;
            int valence = atomValence(atom);
            if ((i + j) % 2 == 0) {
                addEdge(0, vertexID(i, j), valence);
                totalSourceValence += valence;
                if (i + 1 < height) addEdge(vertexID(i, j), vertexID(i + 1, j), 1);
                if (j + 1 < width) addEdge(vertexID(i, j), vertexID(i, j + 1), 1);
                if (i > 0) addEdge(vertexID(i, j), vertexID(i - 1, j), 1);
                if (j > 0) addEdge(vertexID(i, j), vertexID(i, j - 1), 1);
            } else {
                addEdge(vertexID(i, j), numVertices - 1, valence);
                totalSinkValence += valence;
            }
        }
    }
}

int pushFlow(Graph& graph, int current, int flowCapacity) {
    graph.visited[current] = true;
    if (current == graph.numVertices - 1) {
        maxFlow += flowCapacity;
        return flowCapacity;
    }

    for (Edge& edge : graph.edges[current]) {
        if (graph.visited[edge.to] || edge.capacity == 0) {
            continue;
        }

        int bottleneck = pushFlow(graph, edge.to, min(flowCapacity, edge.capacity));
        if (bottleneck > 0) {
            edge.capacity -= bottleneck;
            int reverseEdgeIndex = findReverseEdgeIndex(graph, edge);
            if (reverseEdgeIndex != -1) {
                graph.edges[edge.to][reverseEdgeIndex].capacity += bottleneck;
            } else {
                graph.edges[edge.to].emplace_back(edge.to, edge.from, bottleneck);
            }
            return bottleneck;
        }
    }

    return 0;
}

int main() {
    int height, width;
    cin >> height >> width;
    Graph graph(height, width);
    graph.initializeGraph();

    while (pushFlow(graph, 0, INT_MAX)) {
        graph.resetVisited();
    }

    if (maxFlow == totalSourceValence && maxFlow == totalSinkValence && maxFlow != 0) {
        cout << "Valid" << endl;
    } else {
        cout << "Invalid" << endl;
    }

    return 0;
}