
{pkgs}: {
  deps = [
    pkgs.zeromq
    pkgs.glibcLocales
    pkgs.rustc
    pkgs.libiconv
    pkgs.cargo
    pkgs.jupyter
    pkgs.python312Packages.jupyter-core
    pkgs.python312Packages.notebook
    pkgs.libxcrypt
  ];
}
