import networkx as nx
import matplotlib.pyplot as plt
import json
import scipy

def plot_graph_old(graph, title):
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.title(title)
    plt.savefig(title + ".png")
    plt.show()

#这个函数绘制的标签会重叠
def plot_graph_old2(graph, title):
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(graph)

    # 为节点添加标签（怀疑度）
    labels = {}
    for node, data in graph.nodes(data=True):
        labels[node] = "{}\n{:.2f}".format(node, data['suspicion'])

    nx.draw(graph, pos, labels=labels, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.title(title)
    plt.savefig(title + ".png")

    #显示图片
    #plt.show()
    plt.close()

def plot_graph(graph, title):
    plt.figure(figsize=(12, 10))
    pos = nx.spring_layout(graph)

    # 根据怀疑度计算节点大小
    node_sizes = [data['suspicion'] * 2000 for _, data in graph.nodes(data=True)]

    # 绘制图形，但不绘制标签
    nx.draw(graph, pos, with_labels=False, node_color='lightblue', edge_color='gray', node_size=node_sizes)

    # 计算标签的位置偏移，以减少重叠
    label_pos = {key: [value[0], value[1]+0.05] for key, value in pos.items()}

    # 为节点添加标签（怀疑度）
    labels = {}
    for node, data in graph.nodes(data=True):
        labels[node] = "{}\n{:.2f}".format(node, data['suspicion'])

    # 使用微调过的位置来绘制标签
    nx.draw_networkx_labels(graph, label_pos, labels=labels)

    plt.title(title)
    plt.savefig("result/"+title + ".png")
    plt.close()  # 关闭当前图形

def create_graph_from_json(data):
    G = nx.DiGraph()

    # 添加节点和初始怀疑度
    for node in data['nodes']:
        G.add_node(node['id'], suspicion=node['suspicion'])

    # 添加边
    for relation in data['relations']:
        G.add_edge(relation['from'], relation['to'])

    return G


def compute_pagerank(G):
    pr = nx.pagerank(G)
    for node in G.nodes():
        G.nodes[node]['suspicion'] = pr[node]
    return G

def output_suspicion_to_file(G, filename):
    # 按怀疑度从高到低对节点排序
    sorted_nodes = sorted(G.nodes(data=True), key=lambda x: x[1]['suspicion'], reverse=True)

    with open(filename, 'w') as file:
        for node, data in sorted_nodes:
            file.write("{}: {:.2f}\n".format(node, data['suspicion']))

def main():
    # 读取JSON
    with open("input.json", "r") as file:
        data = json.load(file)

    # 创建图
    G = create_graph_from_json(data)

    # 绘制初始关系图
    plot_graph(G, "Initial Graph")

    # 计算PageRank
    G = compute_pagerank(G)

    # 绘制更新后的关系图
    plot_graph(G, "Updated Graph with PageRank")

    # 输出最终怀疑度到文件
    output_suspicion_to_file(G, "result/final_suspicion.txt")


if __name__ == "__main__":
    main()
