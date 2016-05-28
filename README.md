# practical_tools
practical tools helps to raise productivity. 

该repo用于存放各种帮助大家提高生产力的小工具。

默认您知晓工具提及的使用环境。

## app更新上传蒲公英并邮件通知QA组脚本

环境：```Python3```, 第三方依赖:```requests```

该文件夹下为上传app到蒲公英并邮件通知QA组的脚本：

1. ```upload_to_pgy```为上传app到蒲公英分发平台的脚本
2. ```daily_email_to_QA```为发邮件给QA所有人的脚本
3. ```upload_to_pgy_then_email_to_QA```为上传app到蒲公英并发邮件通知QA的集合脚本

#### 使用方法

1. clone该文件夹并重命名为app的名词如：安邦物业app
2. 修改```daily_email_to_QA```中的```from_addr```和```password```为自己的邮箱密码
3. 修改```upload_to_pgy_then_email_to_QA```中的
	
	```
	app_base_name = "安邦物业app"
	update_file_name = "每日bug.txt"
	upload_file_name = "app.apk"
	```
	为对应的app名称。
4. 将要上传的apk文件或者是ipa文件以及每日修复bug汇总```每日bug.txt```复制到该文件夹下
5. cd 到该目录并执行```python3 upload_to_pgy_then_email_to_QA```