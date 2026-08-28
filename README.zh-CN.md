# Use PowerShell Safely

[English](README.md)

本仓库是 `use-powershell-safely` 的独立本地产品仓库。可安装包位于
[`skills/use-powershell-safely/`](skills/use-powershell-safely/)，其字节与源提交
`80910a8b2375a11be897e9660c4b00a06d00dd13` 完全一致。

## v0.3.0 public Release

独立版本 [`v0.3.0` public Release](https://github.com/junwei529/use-powershell-safely/releases/tag/v0.3.0)
使用公开身份 `junwei529/use-powershell-safely`。其精确 package tree 为
`7e10775d423bfb08bc4ad6388875b7277ce3c18c`；候选只增加独立仓库资格验证和
release lifecycle 材料，不改变 package 行为。

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
