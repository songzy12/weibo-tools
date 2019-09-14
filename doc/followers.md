## 微博 API

<https://open.weibo.com/wiki/微博API>

## followers

获取用户粉丝列表：

<https://open.weibo.com/wiki/2/friendships/followers>

API：

<https://api.weibo.com/2/friendships/followers.json>

|              | 必选  |  类型  |                             说明                             |
| :----------: | :---: | :----: | :----------------------------------------------------------: |
| access_token | true  | string |        采用OAuth授权方式为必填参数，OAuth授权后获得。        |
|     uid      | false | int64  |                     需要查询的用户UID。                      |
| screen_name  | false | string |                     需要查询的用户昵称。                     |
|    count     | false |  int   |          单页返回的记录条数，默认为5，最大不超过5。          |
|    cursor    | false |  int   | 返回结果的游标，下一页用返回值里的next_cursor，上一页用previous_cursor，默认为0。 |
| trim_status  | false |  int   | 返回值中user字段中的status字段开关，0：返回完整status字段、1：status字段仅返回status_id，默认为1。 |

> - 参数uid与screen_name二者必选其一，且只能选其一；
> - 接口升级后：uid与screen_name只能为当前授权用户；

## access_token 

采用OAuth授权方式为必填参数，OAuth授权后获得。

授权机制说明：

<https://open.weibo.com/wiki/%E6%8E%88%E6%9D%83%E6%9C%BA%E5%88%B6%E8%AF%B4%E6%98%8E>

### 开发者自身的授权

这里可以直接使用 接口测试工具 获取 开发者自身的授权。

<https://open.weibo.com/tools/console>

```
access_token = "x"
```

## followers/ids

获取用户粉丝的用户UID列表：

<https://open.weibo.com/wiki/2/friendships/followers/ids>

API：

<https://api.weibo.com/2/friendships/followers/ids.json>

```
uid = 0
```