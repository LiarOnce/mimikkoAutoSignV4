# mimikkoAutoSignV4

用于兽耳桌面相关V4接口测试
不要到处宣传 偷偷用就行了 应该不会封号吧

## 使用

1. 安装依赖 `pip install -r requirements.txt`
2. 抓包软件获取登录时的 `device-id`,`authorization`
3. 修改 `config.yaml`相关设置当前已支持功能  
   | Task                | 功能         | 参数                        | 说明                             |
   | ------------------- | ------------ | --------------------------- | -------------------------------- |
   | Sign                | 每日签到     | `character_code`见下表    | 日常签到，希望不要断连签         |
   | EnergyExchange      | 成长值兑换   | `character_code`见下表    | 包含助手升级以及领取奖励         |
   | EnergyCenter        | 能源中心     | -                           | 默认硬币换电力                   |
   | OrdinaryWork        | 工会悬赏任务 | `work_characters`见下表   | 电力换硬币，积累公会等级         |
   | Task                | 每日任务     | `task_characters`见下表   | 完成任务获得成长值               |
   | MailReceive         | 邮件领取     | -                           | 邮件奖励一键领取                 |
   | ActivitySign        | 活动签到     | -                           | 活动签到                         |
   | UpdateCharacterJson | 助手更新     | -                           | 更新 `助手列表.json`，务必启用 |
   | Travel              | 助手出游     | `travel_characters`见下表 | 旅行收集纪念品                   |

   | 助手名称   | code                      |
   | ---------- | ------------------------- |
   | 诺诺纳     | character_nonona          |
   | 优莉卡     | character_ulrica          |
   | 梦梦奈     | character_momona          |
   | 琉璃       | character_ruri            |
   | 爱莉安娜   | character_ariana          |
   | 阿尔法零   | character_alpha0          |
   | 卡斯塔莉娅 | character_kasutaria       |
   | 卡斯塔莉莉 | character_castariri       |
   | 奈姆利     | character_nemuri          |
   | 胡桃       | character_kurumi          |
   | 羲和       | character_giwa            |
   | 摩耶       | character_maya            |
   | 苏纳       | character_suna            |
   | 米璐库     | character_miruku          |
   | 米露可     | character_miruku2         |
   | 食蜂操祈   | character_shokuhou_misaki |
   | 御坂妹妹   | character_sisters         |
   | 中野一花   | character_nakanoichika    |
   | 中野二乃   | character_nakanonino      |
   | 中野三玖   | character_nakanomiku      |
   | 中野四叶   | character_nakanoyotsuba   |
   | 中野五月   | character_nakanoitsuki    |
   | 御坂美琴   | character_misakamikoto    |
   | 白井黑子   | character_shiraikuroko    |
   | 托尔       | character_tooru           |
   | 康娜       | character_kanna           |
   | 阿波连玲奈 | character_reina           |
   | 环古达     | character_tamakikotatsu   |
   | 爱丽丝     | character_alice           |
   | 泠鸢       | character_yousa           |
   | 梅莉       | character_melly           |
   | 衿         | character_eri             |
   | 逢坂大河   | character_aisaka_taiga    |
   | 薇尔莉特   | character_violet          |

   | 物品                       | material_code                                     |
   | :------------------------- | :------------------------------------------------ |
   | 补签卡                     | `_supplementary_signature_card`                 |
   | 工作刷新券                 | `_work_refresh_ticket`                          |
   | 电力充能券                 | `energy_speedup_ticket`                         |
   | 硬币兑换八周年限时时光旅票 | `coin_to_travel_time_invitation_time_limit_8th` |
   | 硬币兑换八周年限时能源罐   | `coin_to_energy_pack_s_time_limit_8th`          |
   | 硬币兑换八周年限时硬币包小 | `coin_to_coin_pack_s_time_limit_8th`            |
4. ``python main.py``

## 青龙面板

如果使用青龙面板管理脚本，请进行以下操作：

1. 在依赖管理界面安装以下 Python 依赖：

```
apscheduler grpcio grpcio-tools protobuf pytz PyYAML
```

2. 指令拉取仓库（可以粘贴在订阅管理中）

```bash
ql repo https://github.com/zfjdhj/mimikkoAutoSignV4.git "main_ql.py" "venv" "main.py|proto|task|util"
```

## 说明

这只是一个脚本，不要期望有太多功能。

## 更新

20240331：

- fix bug：Travel:'ExchangePostcard'
- fix bug：Travel:移动下一区域

20240322：

- CoinMall(硬币商店): add 额外换取活动添加物品
- fix bug

20240320：

- EnergyCenter(能源中心)：add 自动使用电力充能券
- OrdinaryWork(公会悬赏)：add 自动使用工作刷新券
- OrdinaryWork(公会悬赏)：add 优先完成低等级耗时少的任务
- Travel(助手出游): add 旅行区域满人跳转下一区域
- Travel(助手出游): add 明信片兑换
- Travel(助手出游): add 自行添加助手指定区域出游
