"""
blog历史执行sql留痕
"""


# 创建数据库
CREATE DATABASE myblog;

USE myblog;


# 新增字段，设置初始数据类型，默认值，注释
# ALTER TABLE article_content ADD c_user_id
# INT NOT NULL COMMENT "作者id";

# ALTER TABLE article_content ADD c_state 
# VARCHAR(50) NOT NULL DEFAULT "123123" COMMENT "状态";

# 查看表结构
# DESC article_content;


# DROP TABLE article_content;

CREATE TABLE `article_content` (
	`c_id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '文章id',
	`c_content` VARCHAR(2000) NULL DEFAULT NULL COMMENT '文章内容',
	`c_date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '发布时间',
	`c_views` INT NOT NULL DEFAULT 0 COMMENT "浏览量",
	`c_comment_nums` INT NOT NULL DEFAULT 0 COMMENT '评论数',
	`c_title` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`c_user_id` INT NOT NULL COMMENT '作者id'
)
COMMENT='文章主表'
ENGINE=InnoDB
AUTO_INCREMENT=0
;

# 修改字段数据类型及长度
# ALTER TABLE article_content MODIFY COLUMN c_title VARCHAR(50);

# 删除字段
# ALTER TABLE article_content DROP COLUMN c_state;

# DESC article_content;


# 创建user_info表
CREATE TABLE user_info
(
u_id INT PRIMARY KEY AUTO_INCREMENT COMMENT "作者id",
u_name CHAR(50) NOT NULL COMMENT "用户名",
u_age INT NULL COMMENT "年龄",
u_createdate TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT "加入时间",
u_pseudonym CHAR(50) NULL COMMENT "笔名",
u_is_author INT NOT NULL DEFAULT 0 COMMENT "是否为文章发表者"

)
COMMENT="用户信息表"
ENGINE=INNODB 
AUTO_INCREMENT=0;

# 删除表
# DROP TABLE user_info;

# DESC user_info;

ALTER TABLE user_info ADD PASSWORD CHAR(30) NOT NULL COMMENT "用户密码";

ALTER TABLE user_info CHANGE PASSWORD password CHAR(30);