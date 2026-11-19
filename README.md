# pairwise-injection-query

## 题面

高流量下按条件检索数据时拼接逻辑被注入：用户输入直接拼进 SQL 字符串未参数化；字符串字面量转义缺失可闭合引号；允许一次执行多条语句；LIKE 与排序字段未转义通配符与标识符；输入先入库再拼接形成二次注入。query/builder.py 是核心，tests/test_builder.py 15个红。要修的是：全部参数走占位符绑定；对字面量做正确转义；禁止多语句执行；转义 LIKE 通配符并白名单排序字段；入库前与出库后两次校验阻断二次注入。

## 运行方式

```bash
python -m pytest tests -q
```

初始状态应为 `15 failed`，无 collection error；`tests/` 目录不可修改。

## 字段

- 所属领域：安全
- 子方向：漏洞检测与攻防
- 任务类型：Bugfix
- 语言/框架：Python 3, pytest
- 环境可复现等级：无外部依赖
