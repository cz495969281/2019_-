### 聚合
> 就是用于统计数据，可以按照自己的想法去最终统计数据

```
$match
db.stu.aggregate([
	{
		//过滤管道
		$match:{
			//过滤条件
			age:{$gt:20}
		}
	},

	{
		$group:{
			"_id":"$gender",
			"counter":{$sum:1}
		}
	}
])
```


>$project  管道
```js
db.stu.aggregate([
	{
		//过滤管道
		$match:{
			//过滤条件
			age:{$gt:20}
		}
	},

	{
		$group:{
			"_id":"$gender",
			"counter":{$sum:1}
		}
	},

	{
		$project:{
			"_id":0,
			"counter":1
		}
	}
])

```

>$sort 管道
```js
db.stu.aggregate([
	{
		//过滤管道
		$match:{
			//过滤条件
			age:{$gt:20}
		}
	},

	{
		//参数1表示升序排列
		//参数-1表示降序排列
		$sort:{
			age:1
		}
	}
])
```

>$limit和$skip,注意有先后顺序之分

```js
db.stu.aggregate([
	{
		//过滤管道
		$match:{
			//过滤条件
			gender:true
		}
	},

	{
		$limit:2
	}
])
```

```js
db.stu.aggregate([
	{
		//过滤管道
		$match:{
			//过滤条件
			gender:true
		}
	},

	{
		$skip:1
	},
	{
		$limit:2
	}
])
```

>`$unwind` 管道，拆分列表数据
```js
db.t2.aggregate([
	{
		$unwind:"$size"
	}

])
```

```js
db.t3.aggregate([
	{
		//默认情况下拆分如果是null,空列表，不存在字段等等，就过滤这些数据
		$unwind:"$size",
		//是否显示空数据
		preserveNullAndEmptyArrays:true
	}

])
```

索引
>提高查询效率  缺点：更新，插入，性能下降，重新生成索引
```
//创建索引
db.t1.ensureIndex({字段名:1})
```
//显示索引列表
db.t1.getIndexes()

//删除索引
db.t1.dropIndex("索引的名字")


###备份
mongodump -h 127.0.0.1 -d(数据库名称) admin -o(备份路径) /home/yl

###恢复
 mongorestore -h(主机) 127.0.0.1 -d(数据库名称) admin --dir(数据恢复路径) /home/yl/admin/


 ```js

 db.stu.find(
	
	{
		$where:function(){
			if(this.gender == false){
				return this.age<20 || this.age>40
			}else{
				return this.age>30
			}
		}
	}

 )
 ```

