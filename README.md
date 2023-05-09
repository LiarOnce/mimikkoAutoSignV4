# mimikkoAutoSignV4  
用于兽耳桌面相关V4接口测试  
不要到处宣传 偷偷用就行了 应该不会封号吧
## 使用
1. 抓包软件获取登录时的`device-id`,`authorization`  
2. 修改`config.yaml`相关设置  
    当前已支持功能  
    |Task|功能|参数|说明|
    |-|-|-|-|
    |Sign|每日签到|`character_code`见下表|日常签到，希望不要断连签|
    |EnergyExchange|成长值兑换|`character_code`见下表|-|
    |EnergyCenter|能源中心|-|默认硬币换电力|  
    |OrdinaryWork|工会悬赏任务|`work_characters`见下表|电力换硬币，积累公会等级|  
    |Task|每日任务|`task_characters`见下表|完成任务获得成长值|

    | 助手名称 | code |
    | :- | :- |
    | 魔女日记 | nononabook |
    | 诺诺纳 | nonona |
    | 梦梦奈 | momona |
    | 爱莉安娜 | ariana |
    | 米璐库 | miruku |
    | 奈姆利 | nemuri |
    | 琉璃 | ruri |
    | 阿尔法零 | alpha0 |
    | 米露可 | miruku2 |
    | 优莉卡 | ulrica |
3. ```python main.py```
## 说明
这只是一个脚本，不要期望有太多功能。