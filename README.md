```markdown
# Agent Project — 从 Mini Agent 到 LangGraph + RAG Agent

一个从 **0 到 1 构建 AI Agent 系统**的实践项目，涵盖：

- 手写 Agent（理解本质）
- LangChain Agent（框架使用）
- Memory（对话能力）
- LangGraph（可控工作流）
- Tool 系统（工具调用）
- RAG（知识检索能力）

---

# 项目亮点（Highlights）
从底层手写 Agent loop，理解 ReAct 模式  
支持 Tool 调用（计算器 / 时间 / 字典 / RAG）  
集成 Memory，实现多轮对话  
基于 LangGraph 构建可控 Agent Workflow  
将 RAG 封装为 Tool，实现知识型 Agent  

---

# Agent 核心架构

Agent 本质：
```

LLM + Tool + Memory + Decision Loop

```
项目中实现了完整流程：
```

User
↓
LLM（决策）
↓
Tool Selection
↓
Tool Execution
↓
Observation
↓
LLM总结

---

## 项目结构

Agent_project/
│
├── agent/
│ ├── mini_agent.py # 手写 Agent（理解原理）
│ └── langchain_agent.py # LangChain Agent
│
├── graph/
│ ├── simple_graph.py # 基础 LangGraph
│ ├── agent_graph.py # Tool + Agent Graph
│ └── tool_node.py # Tool 调用节点
│
├── tools/
│ ├── calculator.py
│ ├── dictionary.py
│ ├── time.py
│ ├── rag_tool.py # ⭐ RAG Tool
│ └── tool_registry.py # Tool 注册中心
│
├── llm/
│ └── dashscope_llm.py # LLM 封装
│
├── main.py # Mini Agent
├── main_langchain.py # LangChain Agent
├── main_memory.py # Memory Agent
├── main_graph.py # LangGraph 基础版
├── main_graph_tool.py # ⭐ 最终 Agent（带 Tool + RAG）
│
└── requirements.txt

---

## 功能演进（学习路径）

---

### Stage 1 — Mini Agent（手写）

```bash
python3 main.py
```

实现：

- 手写 Agent Loop
- 理解 ReAct Pattern

------

### Stage 2 — LangChain Agent

```bash
python3 main_langchain.py
```

实现：

- Tool 调用（自动）
- LLM 决策

------

### Stage 3 — Memory（对话能力）

```bash
python3 main_memory.py
```

实现：

- 多轮对话
- 上下文记忆

------

### Stage 4 — LangGraph（工作流控制）

```bash
python3 main_graph.py
```

实现：

- 状态驱动 Agent
- Graph 控制流程

------

### Stage 5 — Tool + RAG Agent（最终版本）

```bash
python3 -m main_graph_tool
```

实现：

- Tool 调度系统
- RAG 作为 Tool
- 知识型 Agent

------

## RAG 设计（核心）

------

###  RAG Pipeline

```
Query
 ↓
Embedding
 ↓
FAISS
 ↓
Retriever
 ↓
Context
 ↓
LLM
```

------

###  RAG Tool 化

```python
def knowledge_base_search(query: str) -> str:
    docs = retriever.invoke(query)
    return "\n\n".join(doc.page_content for doc in docs)
```

------

###  在 Agent 中的作用

```
User: 根据知识库回答...
 ↓
Agent 判断
 ↓
调用 knowledge_base_search
 ↓
返回上下文
 ↓
LLM生成答案
```

------

##  Tool 系统设计

项目采用：

```python
TOOLS = {
    "calculator": calculator,
    "dictionary": dictionary,
    "time": time,
    "knowledge_base_search": knowledge_base_search
}
```

------

### 设计思想

- Tool = 可调用函数
- Agent 负责决策
- tool_node 负责执行

实现：

```
LLM → tool_name → function → result
```

------

## 技术要点总结

------

### 1. ReAct 模式

```
Thought → Action → Observation → Final Answer
```

------

### 2. LangChain 新架构

- 所有组件 = Runnable
- 使用 `.invoke()` 调用

------

### 3. RAG 本质

```
RAG = 一个知识检索工具
```

------

### 4. Agent 本质

```
Agent = 会使用工具的 LLM
```

------

## 安装与运行

------

### 创建虚拟环境

```bash
python3 -m venv venv
source venv/bin/activate
```

------

### 安装依赖

```bash
pip install -r requirements.txt
```

------

### 运行项目

```bash
python3 -m main_graph_tool
```

------

## 注意事项

------

### HuggingFace 模型下载慢

```bash
export HF_ENDPOINT=https://hf-mirror.com
```

------

### FAISS 安装问题

```bash
pip install faiss-cpu
```

------

## 项目总结

本项目完整实现了：

```
Mini Agent → LangChain Agent → Memory → LangGraph → Tool → RAG Agent
```

实现了一个具备：

- 工具调用能力
- 对话能力
- 知识检索能力

的 **AI Agent 系统原型**