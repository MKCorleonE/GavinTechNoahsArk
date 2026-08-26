# 04_RAG
> 本章节主要介绍了RAG（Retrieval-Augmented Generation）相关的理论知识和开发语言。
## 什么是RAG
RAG（Retrieval-Augmented Generation）是一种结合了检索和生成的自然语言处理技术。它通过在生成文本的过程中引入外部知识库或文档检索机制，从而提高生成文本的准确性和丰富性。RAG模型通常由两个主要组件组成：检索器（Retriever）和生成器（Generator）。检索器负责从外部知识库中找到与输入相关的信息，而生成器则根据这些信息生成最终的输出文本。
### RAG的工作流程图：
```
                    用户问题
                       │
                       ▼
                ┌─────────────┐
                │ Query处理   │
                └──────┬──────┘
                       │
                       ▼
                ┌─────────────┐
                │ Retriever   │
                │    检索      │
                └──────┬──────┘
                       │
              ┌────────┴────────┐
              ▼                 ▼
          向量检索           BM25检索
              │                 │
              └────────┬────────┘
                       ▼
                ┌─────────────┐
                │ Reranker    │
                │   重排序     │
                └──────┬──────┘
                       │
                       ▼
                ┌─────────────┐
                │ Prompt构造  │
                └──────┬──────┘
                       │
                       ▼
                ┌─────────────┐
                │     LLM     │
                └──────┬──────┘
                       │
                       ▼
                     答案

```

### RAG的离线构建流程图
```
原始文档
   │
   ▼
文档加载
   │
   ▼
文本清洗
   │
   ▼
Chunk切分
   │
   ▼
Embedding
   │
   ▼
向量数据库
   │
   ▼
Retriever
```
### 完整的RAG包含：
```
                【离线阶段】
                    
文档
 │
 ▼
Document Loader
 │
 ▼
Text Cleaning
 │
 ▼
Chunking
 │
 ▼
Embedding
 │
 ▼
Vector Database
 │
 └────────────────────────┐
                          │
                【在线查询阶段】
                          │
用户问题 ──→ Query处理 ──→ Retriever
                          │
                          ▼
                       Reranker
                          │
                          ▼
                    Context构建
                          │
                          ▼
                         LLM
                          │
                          ▼
                         答案
```

## 本章节包含
- 4.1 RAG基础
- 4.2 文档处理与Chunking
- 4.3 Embedding与向量数据库
- 4.4 Retriever检索
- 4.5 Reranker重排序
- 4.6 Prompt与Context构建
- 4.7 RAG完整Pipeline
- 4.8 RAG评估
- 4.9 高级RAG
- 4.10 RAG工程化