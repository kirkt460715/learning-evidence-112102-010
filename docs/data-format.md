# 记录格式

学习者表达记录以 id、course、indicator、source、instrument、coverage、value 描述指标来源、工具版本、覆盖范围及观测值。

记录以 UTF-8 JSON 保存，顶层包含 dataset 和 records。每条记录的 id 在文件中唯一。`fixtures/records.json` 中的例子用于说明输入字段和状态取值。
