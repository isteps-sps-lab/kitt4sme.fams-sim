{
  inputs = {
    nixie.url = "github:c0c0n3/nixie";
    nixpkgs.follows = "nixie/nixpkgs";
  };

  outputs = { self, nixpkgs, nixie }:
  let
    output = nixie.lib.flakes.mkOutputSetForCoreSystems nixpkgs;
    devEnv = { system, sysPkgs, ...}: {
      defaultPackage.${system} = with sysPkgs; buildEnv {
        name = "fipy-dev-env";
        paths = [ python3 poetry ];
      };
    };
  in
    output devEnv;
}
