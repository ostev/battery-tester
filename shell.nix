{ pkgs ? import (fetchTarball https://git.io/Jf0cc) {} }:

let
  customPython = pkgs.python38.buildEnv.override {
    extraLibs = [ pkgs.python38Packages.matplotlib
      pkgs.python38Packages.numpy ];
  };
in

pkgs.mkShell {
  buildInputs = [ customPython ];
}
