// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract SupplyChainKopi {
    enum StatusKopi { Panen, Diproses, Dikirim, Diterima }

    struct Kopi {
        uint id;
        string namaPetani;
        uint256 beratKg;
        StatusKopi status;
        address pemilikSaatIni;
    }
    
    uint256 public totalKopi = 0;

    mapping(uint256 => Kopi ) public daftarKopi;

    function daftarPanenBaru(string memory _namaPetani, uint256 _beratKg) public {
        totalKopi += 1;

        daftarKopi[totalKopi] = Kopi({
            id: totalKopi,
            namaPetani: _namaPetani,
            beratKg: _beratKg,
            status: StatusKopi.Panen,
            pemilikSaatIni: msg.sender
        });
    }

    function updateStatus(uint256 _id, StatusKopi _statusBaru) public {
        require(_id > 0 && _id <= totalKopi, "Kopi tidak ditemukan di sistem");

        require(msg.sender == daftarKopi[_id].pemilikSaatIni, "Ditolak: Anda bukan pemilik kopi ini!");
        daftarKopi[_id].status = _statusBaru;
    }
}