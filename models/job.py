from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from models.company import company
from sqlalchemy.orm import declarative_base

base = declarative_base()

class job(base):
    __tablename__ = "job"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    salary = Column(Integer, nullable=False)
    company_id = Column(Integer, ForeignKey("company.id"))
    company = relationship("company", back_populates="jobs")    raise exc_value.with_traceback(exc_tb)
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\pool\base.py", line 896, in __connect
    self.dbapi_connection = connection = pool._invoke_creator(self)
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\engine\create.py", line 667, in connect
    return dialect.connect(*cargs_tup, **cparams)
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\engine\default.py", line 630, in connect
    return self.loaded_dbapi.connect(*cargs, **cparams)  # type: ignore[no-any-return]  # NOQA: E501
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\psycopg2\__init__.py", line 135, in connect
    conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) connection to server at "localhost" (::1), port 5433 failed: FATAL:  database "Student_db" does not exist

(Background on this error at: https://sqlalche.me/e/20/e3q8)
(env) PS D:\Repos\python_basics\fastapi> uvicorn app.main:app --reload
INFO:     Will watch for changes in these directories: ['D:\\Repos\\python_basics\\fastapi']
Engine(postgresql://postgres:***@localhost:5433/Student_db)
Traceback (most recent call last):
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\engine\base.py", line 144, in __init__
    self._dbapi_connection = engine.raw_connection()
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\engine\base.py", line 3319, in raw_connection
    return self.pool.connect()
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\pool\base.py", line 448, in connect
    return _ConnectionFairy._checkout(self)
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\pool\base.py", line 1272, in _checkout
    fairy = _ConnectionRecord.checkout(pool)
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\pool\base.py", line 712, in checkout
    rec = pool._do_get()
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\pool\impl.py", line 178, in _do_get
    with util.safe_reraise():
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\util\langhelpers.py", line 122, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\pool\impl.py", line 176, in _do_get
    return self._create_connection()
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\pool\base.py", line 389, in _create_connection
    return _ConnectionRecord(self)
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\pool\base.py", line 674, in __init__
    self.__connect()
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\pool\base.py", line 900, in __connect
    with util.safe_reraise():
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\util\langhelpers.py", line 122, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\pool\base.py", line 896, in __connect
    self.dbapi_connection = connection = pool._invoke_creator(self)
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\engine\create.py", line 667, in connect
    return dialect.connect(*cargs_tup, **cparams)
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\engine\default.py", line 630, in connect
    return self.loaded_dbapi.connect(*cargs, **cparams)  # type: ignore[no-any-return]  # NOQA: E501
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\psycopg2\__init__.py", line 135, in connect
    conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
psycopg2.OperationalError: connection to server at "localhost" (::1), port 5433 failed: FATAL:  database "Student_db" does not exist


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "D:\Repos\python_basics\fastapi\env\Scripts\uvicorn.exe\__main__.py", line 7, in <module>
    sys.exit(main())
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\click\core.py", line 1569, in __call__
    return self.main(*args, **kwargs)
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\click\core.py", line 1490, in main
    rv = self.invoke(ctx)
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\click\core.py", line 1353, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\click\core.py", line 907, in invoke
    return callback(*args, **kwargs)
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\uvicorn\main.py", line 441, in main
    run(
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\uvicorn\main.py", line 609, in run
    config.load_app()
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\uvicorn\config.py", line 415, in load_app
    return import_from_string(self.app)
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\uvicorn\importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\importlib\__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "D:\Repos\python_basics\fastapi\app\main.py", line 11, in <module>
    Base.metadata.create_all(bind=engine)
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\sql\schema.py", line 5930, in create_all
    bind._run_ddl_visitor(
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\engine\base.py", line 3269, in _run_ddl_visitor
    with self.begin() as conn:
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\contextlib.py", line 135, in __enter__
    return next(self.gen)
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\engine\base.py", line 3259, in begin
    with self.connect() as conn:
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\engine\base.py", line 3295, in connect
    return self._connection_cls(self)
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\engine\base.py", line 146, in __init__
    Connection._handle_dbapi_exception_noconnection(
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\engine\base.py", line 2450, in _handle_dbapi_exception_noconnection
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\engine\base.py", line 144, in __init__
    self._dbapi_connection = engine.raw_connection()
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\engine\base.py", line 3319, in raw_connection
    return self.pool.connect()
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\pool\base.py", line 448, in connect
    return _ConnectionFairy._checkout(self)
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\pool\base.py", line 1272, in _checkout
    fairy = _ConnectionRecord.checkout(pool)
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\pool\base.py", line 712, in checkout
    rec = pool._do_get()
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\pool\impl.py", line 178, in _do_get
    with util.safe_reraise():
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\util\langhelpers.py", line 122, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\pool\impl.py", line 176, in _do_get
    return self._create_connection()
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\pool\base.py", line 389, in _create_connection
    return _ConnectionRecord(self)
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\pool\base.py", line 674, in __init__
    self.__connect()
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\pool\base.py", line 900, in __connect
    with util.safe_reraise():
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\util\langhelpers.py", line 122, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\pool\base.py", line 896, in __connect
    self.dbapi_connection = connection = pool._invoke_creator(self)
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\engine\create.py", line 667, in connect
    return dialect.connect(*cargs_tup, **cparams)
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\engine\default.py", line 630, in connect
    return self.loaded_dbapi.connect(*cargs, **cparams)  # type: ignore[no-any-return]  # NOQA: E501
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\psycopg2\__init__.py", line 135, in connect
    conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) connection to server at "localhost" (::1), port 5433 failed: FATAL:  database "Student_db" does not exist

(Background on this error at: https://sqlalche.me/e/20/e3q8)
(env) PS D:\Repos\python_basics\fastapi> uvicorn app.main:app --reload
INFO:     Will watch for changes in these directories: ['D:\\Repos\\python_basics\\fastapi']
Engine(postgresql://postgres:***@localhost:5433/Student_db)
Traceback (most recent call last):
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\engine\base.py", line 144, in __init__
    self._dbapi_connection = engine.raw_connection()
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\engine\base.py", line 3319, in raw_connection
    return self.pool.connect()
  File "D:\Repos\python_basics\fastapi\env\lib\site-packages\sqlalchemy\pool\base.py", line 448, in connect
    return _ConnectionFairy._checkout(self)