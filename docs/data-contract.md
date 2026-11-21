# 数据说明

民情问题分类、口径版本及历史分析解释的本地合成资料。

下列文件仅包含合成记录。空值按 CSV 空单元格保存；时间字段使用当地业务记录时间，不预设统计结论。

## `categories.csv`

字段：`category_id`、`label`、`valid_from`、`valid_to`。当前演练样本 4 条。

## `mapping.csv`

字段：`mapping_id`、`old_category`、`new_category`、`coverage`、`review_state`、`valid_from`。当前演练样本 3 条。

## `classified_requests.csv`

字段：`request_id`、`category_id`、`classified_at`、`reviewer_ref`、`source_ref`。当前演练样本 4 条。

## `reports.csv`

字段：`report_id`、`period`、`definition_version`、`published_at`。当前演练样本 2 条。
