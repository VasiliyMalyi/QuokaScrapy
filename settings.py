BOT_NAME = 'TaskSolve'

SPIDER_MODULES = ['TaskSolve.spiders']
NEWSPIDER_MODULE = 'TaskSolve.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'TaskSolve.pipelines.QuokaPipeline': 0,
}
