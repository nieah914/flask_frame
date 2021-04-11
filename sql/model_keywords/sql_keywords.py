from common.dbcon import DBO
from common import utils
import time
class QueryManager(DBO, utils.Utills):
    def __init__(self,_user_id):
        super().__init__(_user_id)
        self.user_id = _user_id

    def getKeywords(self,_item):
        self.print_common_log()
        try:
            query = '''
            SELECT 
                `t_anal_keywords`.`keyword`
            FROM `blog_db`.`t_anal_keywords`
              WHERE 1 = 1
                AND sts <> 'D'
                AND user_id = {0}
                '''
            query.format(_item['usr_id'])
            return self.getQueryList(query)
        except Exception as e:
            self.print_error_log(str(e))

    def getWebHistories(self,_item):
        self.print_common_log()
        try:
            return self.getQueryList(
                '''
            SELECT 
                `t_analysis_datas`.`keyword`,
                `t_analysis_datas`.`post_url`,
                `t_analysis_datas`.`blog_id`,
				(select rank from t_analysis_datas B where B.keyword = t_analysis_datas.keyword
										and B.post_url = t_analysis_datas.post_url
										and date(B.reg_dt) = date(t_analysis_datas.reg_dt) - INTERVAL  1 DAY
										and B.reg_date = t_analysis_datas.reg_date
										and B.user_id = t_analysis_datas.user_id
										and B.mobile_yn = t_analysis_datas.mobile_yn) as `rank_yesterday`,
                `t_analysis_datas`.`rank`,
                `t_analysis_datas`.`total_words`,
                `t_analysis_datas`.`img_cnt`,
                `t_analysis_datas`.`video_cnt`,
                `t_analysis_datas`.`video_running_time`,
                `t_analysis_datas`.`somenail_type`,
                `t_analysis_datas`.`avr_visits`,
                `t_analysis_datas`.`reg_date`,
                `t_analysis_datas`.`tags`,
                `t_analysis_datas`.`keywords_cnt_in_tags`,
                `t_analysis_datas`.`total_post`,
                `t_analysis_datas`.`keywords_cnt_in_title`,
                `t_analysis_datas`.`title`,
                `t_analysis_datas`.`keywords_cnt_in_contents`,
                `t_analysis_datas`.`clipboards_cnt`,
                `t_analysis_datas`.`somenail_cnt`,
                `t_analysis_datas`.`map_counts`,
                `t_analysis_datas`.`reg_dt`,
                `t_analysis_datas`.`is_influencer`,
                `t_analysis_datas`.`user_id`
            FROM `blog_db`.`t_analysis_datas`
              WHERE user_id = %s
                AND mobile_yn = 'N'
                AND date(reg_dt) = %s
                    order by keyword,rank
                '''
                , (_item['id'], _item['yyyymmdd'])
            )
        except Exception as e:
            self.print_error_log(str(e))

    def getMobileHistories(self,_item):
        self.print_common_log()
        try:
            return self.getQueryList(
                '''
            SELECT 
                `t_analysis_datas`.`keyword`,
                `t_analysis_datas`.`post_url`,
                `t_analysis_datas`.`blog_id`,
                '' as rank_yesterday,
                `t_analysis_datas`.`rank`,
                `t_analysis_datas`.`total_words`,
                `t_analysis_datas`.`img_cnt`,
                `t_analysis_datas`.`video_cnt`,
                `t_analysis_datas`.`video_running_time`,
                `t_analysis_datas`.`somenail_type`,
                `t_analysis_datas`.`avr_visits`,
                `t_analysis_datas`.`reg_date`,
                `t_analysis_datas`.`tags`,
                `t_analysis_datas`.`keywords_cnt_in_tags`,
                `t_analysis_datas`.`total_post`,
                `t_analysis_datas`.`keywords_cnt_in_title`,
                `t_analysis_datas`.`title`,
                `t_analysis_datas`.`keywords_cnt_in_contents`,
                `t_analysis_datas`.`clipboards_cnt`,
                `t_analysis_datas`.`somenail_cnt`,
                `t_analysis_datas`.`map_counts`,
                `t_analysis_datas`.`reg_dt`,
                `t_analysis_datas`.`is_influencer`,
                `t_analysis_datas`.`user_id`
            FROM `blog_db`.`t_analysis_datas`
                WHERE user_id = %s
                AND 1 = 1
                AND date(reg_dt) = %s
                AND mobile_yn = 'Y'
                    
                    order by keyword,rank
                '''
                , (_item['id'], _item['yyyymmdd'])
            )
        except Exception as e:
            self.print_error_log(str(e))


    def getProgramInfo(self,_item):
        self.print_common_log()
        try:
            return self.getQuery(
                '''
                SELECT sts,title FROM t_program where id = %s
                '''
                ,_item['id']
            )
        except Exception as e:
            self.print_error_log(str(e))

    def deleteTodayHistory(self,_item):
        self.print_common_log()
        self.update(
            '''
            DELETE FROM t_analysis_datas WHERE  `reg_dt` = %s
            ''',[time.strftime('%Y%m%d')])

    def addHistory(self,_item):
        self.print_common_log()



        self.update(
            '''
             INSERT INTO `blog_db`.`t_analysis_datas`
            (   
               `keyword`,
                `post_url`,
                `blog_id`,
                `rank`,
                `total_words`,
                `img_cnt`,
                `video_cnt`,
                `video_running_time`,
                `somenail_type`,
                `avr_visits`,
                `reg_date`,
                `tags`,
                `keywords_cnt_in_tags`,
                `total_post`,
                `keywords_cnt_in_title`,
                `title`,
                `keywords_cnt_in_contents`,
                `clipboards_cnt`,
                `somenail_cnt`,
                `map_counts`,
                `is_influencer`,
                `user_id`,
                `mobile_yn`,
                `reg_dt`
            )
            VALUES(
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s)
            ON DUPLICATE KEY 
            UPDATE 
             `keyword`= %s,
                `post_url`= %s,
                `blog_id`= %s,
                `rank`= %s,
                `total_words`= %s,
                `img_cnt`= %s,
                `video_cnt`= %s,
                `video_running_time`= %s,
                `somenail_type`= %s,
                `avr_visits`= %s,
                `reg_date`= %s,
                `tags`= %s,
                `keywords_cnt_in_tags`= %s,
                `total_post`= %s,
                `keywords_cnt_in_title`= %s,
                `title`= %s,
                `keywords_cnt_in_contents`= %s,
                `clipboards_cnt`= %s,
                `somenail_cnt`= %s,
                `map_counts`= %s,
                `is_influencer`= %s,
                `user_id` = %s,
                `mobile_yn` = %s,
                `reg_dt` = %s
            '''
            , [_item['keyword'],_item['post_url'],_item['blog_id'],_item['rank_no'],_item['total_words'],
               _item['image_cnt'],_item['video_num'],_item['running_time'],_item['thumb_type']
               ,_item['avr_visits_num'],_item['target_date'],_item['tags'],_item['keywords_cnt'],
               _item['total_post'],_item['keyword_count_in_title'],_item['title'],_item['keyword_count_in_contents']
               ,_item['clipe_cnt'],_item['thumb_count'],_item['map_cnt'],_item['is_influencer'],self.user_id,_item['mobile_yn'],time.strftime('%Y%m%d')

               ,_item['keyword'], _item['post_url'], _item['blog_id'], _item['rank_no'], _item['total_words'],
               _item['image_cnt'], _item['video_num'], _item['running_time'], _item['thumb_type']
                , _item['avr_visits_num'], _item['target_date'], _item['tags'], _item['keywords_cnt'],
               _item['total_post'], _item['keyword_count_in_title'], _item['title'], _item['keyword_count_in_contents']
                , _item['clipe_cnt'], _item['thumb_count'], _item['map_cnt'], _item['is_influencer'],self.user_id,_item['mobile_yn'],time.strftime('%Y%m%d')

               ]
        )