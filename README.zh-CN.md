# Use PowerShell Safely

[English](README.md)

**帮助 AI 在 Windows 上把命令执行对。**

Use PowerShell Safely 是面向 Codex 的 Windows 命令执行与故障诊断 Skill。它关注 PowerShell、外部程序、文本文件和 WSL 之间容易出错的连接处，帮助 AI 在执行前检查关键条件、出错后定位原因、执行后核对实际结果。

它适合包含复杂参数、中文路径、文件编码、子进程或 Windows／WSL 交互的任务。

## 它能帮助你

- **执行前检查关键条件。** 根据任务涉及的版本、参数、路径和权限选择合适的命令写法。
- **把问题定位到具体环节。** 区分应用代码、命令解析、参数传递、输出处理和运行环境问题，让修正针对实际原因。
- **核对真正的执行结果。** 检查进程是否结束、退出状态是否可靠，以及输出文件和文本内容是否符合预期。

## 一个使用场景

PowerShell 调用 Python 处理包含中文的 JSON。命令看起来已经结束，输出内容却不正确。

这时需要核对 Python 实际收到的参数、文件的读写编码和进程退出结果，并用最小复现定位问题。确认原因后，再决定该调整命令、环境还是代码。

## 开始使用

执行复杂命令之前：

```text
$use-powershell-safely
我要用 PowerShell 调用 Python，处理包含中文路径的 JSON 文件。
请先检查参数传递、编码和退出状态的处理，再执行已授权的操作。
```

遇到问题之后：

```text
这条命令显示已经结束，但没有得到预期文件。
请先定位失败环节，并说明依据，再提出修正方案。
```

相关运行条件已经确认且没有变化时，可以复用这些证据；按当前问题读取必要的诊断细节。

## 进一步了解

[设计说明](docs/skills/use-powershell-safely/DESIGN.md) ·
[验证范围](docs/skills/use-powershell-safely/VERIFICATION.md) ·
[评估场景](evals/cases/powershell-boundary.md)

<details>
<summary>安装与验证、版本沿革和证据限制</summary>

本仓库是 `use-powershell-safely` 的独立本地产品仓库。规范可编辑 package 位于
[`skills/use-powershell-safely/`](skills/use-powershell-safely/)。冻结的 migration
与 `v0.3.0` baseline 保留了源提交
`80910a8b2375a11be897e9660c4b00a06d00dd13` 的 package 字节；当前 working
source 已包含 [State](docs/skills/use-powershell-safely/STATE.md) 记录的 `0.3.3` 源码增量。

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

## 保留的 0.3.2 本地安装记录

保留的 `0.3.2` 五文件 package 与其 PowerShell boundary case 包含 source-only
增量，覆盖比例化 harness 诊断、wrapper-aware 文本合同、JSON 表示限制、Python
显式 UTF-8 处理及相关 eval。其 package tree 为
`f76f6deaec88101ecdda4c5dbc47405d8b930a65`。用户确认的 `0.3.2` USER
安装当时已完成，五文件与 `0.3.2` source 一致，普通沙箱可读。该副本与更早的 `0.3.1-local.3` 均保留
用于恢复。新任务加载、模型 qualification 与 publication 尚未证明；冻结的
`v0.3.0` 证据保持不变。当前验证入口及保留的历史失败记录见
[Verification](docs/skills/use-powershell-safely/VERIFICATION.md)；当前来源映射为
[`provenance/source-map-v0.3.3.json`](provenance/source-map-v0.3.3.json)。

## 当前 0.3.3 源码

用户确认的 `0.3.3` source 区分命令前的材料边界准备与故障诊断，复用已验证且
未变化的运行环境证据，并仅按实际问题读取引用细节。candidate 是源码验收
快照，不是安装或模型行为证据。独立源码验收与匹配源码的 USER `0.3.3` 更新
已完成。经单独批准，仅恢复安装根目录的 ACL 继承后，普通沙箱已验证五文件、
receipt 与 managed 状态；新任务加载和模型行为仍未验证，详见
[State](docs/skills/use-powershell-safely/STATE.md)。

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

</details>
