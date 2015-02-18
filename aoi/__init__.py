from fuze.context import Context
from aoi import context


Context.__bases__ += (context.Context, )