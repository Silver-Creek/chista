@ECHO OFF

ECHO Clean up In Progree...

@RD /S /Q "pynomial.egg-info"

@RD /S /Q ".vscode"

@RD /S /Q "build"

@RD /S /Q ".pytest_cache"

ECHO Done