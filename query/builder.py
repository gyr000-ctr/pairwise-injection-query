"""builder 核心模块（初始失败环境，待修复）。"""

def build_select(table, conditions):
    """待实现的安全修复入口。"""
    raise NotImplementedError

def escape_literal(value):
    """待实现的安全修复入口。"""
    raise NotImplementedError

def allow_multi_statement(sql):
    """待实现的安全修复入口。"""
    raise NotImplementedError

def escape_like(value):
    """待实现的安全修复入口。"""
    raise NotImplementedError

def safe_order(field, allowed):
    """待实现的安全修复入口。"""
    raise NotImplementedError

def check_stored_input(value):
    """待实现的安全修复入口。"""
    raise NotImplementedError
