# 分类口径与专题调查：资料契约

`register` 的事项号全局唯一；`legacy_reports` 是往期会审已使用的旧口径记录。`mapping` 的同一来源小类候选互斥，每条附一个条件；符合 `always` 代表无条件候选。`attributes` 中空字段表示原登记未收集，`issuer` 为已知不属于新统计母体时填写 `external`；`issuer` 缺失代表范围待证，旧表中曾纳入的记录不能自动视为新版合规。归口变化和版本边界按 `edition` 生效日以及 `scope` 指定的编码解释，不以程序运行时间代替观察期。每条签认可作 `confirmed` 或 `revoked`；明确了适用期及影响的项目后才能决定新版归类或统计资格。`rules` 的 `delta_pp` 是份额差门槛（百分点，达到即触发），`min_count` 为两个时期各自最低母体量。
资料组配额按独立事项计。若一个事项的全部候选不会改变任何当前规则判定，就不入候选；存在多个可行动作时可根据多个规则受影响情况或一组联合证据来解释优先理由。已发专题记录是主任确认事实，不作为归类输入。所有业务时间使用当地时间，左闭右开。

## 输入表

- `editions.csv`：`edition`、`start`、`scope`、`class`、`label`
- `mapping.csv`：`edition`、`legacy_class`、`candidate`、`condition`
- `register.csv`：`item`、`period`、`source_edition`、`source_class`、`purpose`、`issuer`
- `signatures.csv`：`id`、`item`、`edition`、`period`、`field`、`value`、`state`、`prior`、`at`
- `legacy_reports.csv`：`report`、`period`、`edition`、`class`、`count`、`published_at`
- `rules.csv`：`rule`、`edition`、`from_period`、`to_period`、`class`、`delta_pp`、`min_count`、`review_budget`
- `inquiries.csv`：`id`、`rule`、`confirmed_at`、`evidence_cutoff`
