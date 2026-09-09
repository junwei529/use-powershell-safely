# Use PowerShell Safely

[English](README.md)

本仓库是 `use-powershell-safely` 的独立本地产品仓库。规范可编辑 package 位于
[`skills/use-powershell-safely/`](skills/use-powershell-safely/)。冻结的 migration
与 `v0.3.0` baseline 保留了源提交
`80910a8b2375a11be897e9660c4b00a06d00dd13` 的 package 字节；当前 working
source 已包含 [State](docs/skills/use-powershell-safely/STATE.md) 记录的 `0.3.2` 本地增量。

## v0.3.0 public Release

独立版本 [`v0.3.0` public Release](https://github.com/junwei529/use-powershell-safely/releases/tag/v0.3.0)
使用公开身份 `junwei529/use-powershell-safely`。其精确 package tree 为
`7e10775d423bfb08bc4ad6388875b7277ce3c18c`；在该 release 边界，候选只增加
独立仓库资格验证和 release lifecycle 材料，不改变 package 行为。

Exact candidate C 已获验收，并由
[`release/v0.3.0-local-release-receipt.json`](release/v0.3.0-local-release-receipt.json)
绑定，因此 `LOCAL_RELEASE_READY` 为 `VERIFIED`。不可变 candidate descriptor
保留 C 中原始的 `PENDING_PLANNER_ACCEPTANCE` 快照。独立的
[`public-source descriptor`](release/v0.3.0-public-release-candidate.json)
保留不可变的公开前快照。独立的
[`public-release evidence`](release/v0.3.0-public-release-evidence.json) 绑定 public
source commit `13edb84cd1b072cb64926c5ae600714c6f7203e7`、annotated tag
`v0.3.0`、已批准的 non-draft/non-prerelease Release、same-version managed
lifecycle 证据与最终 exact installed copy。该证据主体已由 Planner 以 public
evidence id `B2-PS-PUBLIC-EVIDENCE-F-01` 独立验收。

获验收的 Q04 证明三个冻结场景中的 bounded SOURCE-forward behavior。fresh
projectless witness 分别证明 origin-aware absence，以及唯一 USER-scope exact
installed copy 的 selection、五文件完整加载与同样三个 bounded scenarios。
cross-version lifecycle、live WSL、cross-Harness behavior、untested contexts 与
broad efficacy 仍为 `UNKNOWN`。

## 当前 0.3.2 本地安装

当前五文件 working package 与 PowerShell boundary case 已加入 source-only
增量，覆盖比例化 harness 诊断、wrapper-aware 文本合同、JSON 表示限制、Python
显式 UTF-8 处理及相关 eval。当前 package tree 为
`f76f6deaec88101ecdda4c5dbc47405d8b930a65`。用户确认的 `0.3.2` USER
安装已完成，五文件与 source 一致，普通沙箱可读。旧 `0.3.1-local.3` 副本保留
用于恢复。新任务加载、模型 qualification 与 publication 尚未证明；冻结的
`v0.3.0` 证据保持不变。当前验证入口及保留的历史失败记录见
[Verification](docs/skills/use-powershell-safely/VERIFICATION.md)；当前来源映射为
[`provenance/source-map-v0.3.2.json`](provenance/source-map-v0.3.2.json)。

## 仓库内容

- 产品包：[`skills/use-powershell-safely/`](skills/use-powershell-safely/)
- 产品设计与状态：[`docs/skills/use-powershell-safely/`](docs/skills/use-powershell-safely/)
- 评估 case 与 fixture：[`evals/`](evals/README.md)
- 独立验证：[`scripts/check_repository.py`](scripts/check_repository.py)
- 来源映射：[`PROVENANCE.md`](PROVENANCE.md) 与
  [`provenance/source-map.json`](provenance/source-map.json)

## 验证

```powershell
python -B scripts/check_source_contract.py --json
python -B scripts/manage_install.py self-test --source .
python -B scripts/check_repository.py --json
python -B scripts/check_repository.py --adversarial
pwsh -NoLogo -NoProfile -NonInteractive -File evals/check-powershell-boundaries.ps1
powershell.exe -NoLogo -NoProfile -NonInteractive -File evals/check-powershell-boundaries.ps1
```

Lifecycle 工具默认只做 dry-run；真实操作必须同时给出明确 destination 和
`--apply`。本仓库不隐式依赖其他 Skill 仓库。保留的 public evidence 将 immutable
source、publication、same-version lifecycle 与 loaded-copy behavior 分层；它不主张
cross-version lifecycle、Profile mutation、live WSL、cross-Harness behavior、
untested contexts 或 broad product efficacy。
