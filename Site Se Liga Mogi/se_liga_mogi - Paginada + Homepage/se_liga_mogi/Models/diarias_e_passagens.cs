//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated from a template.
//
//     Manual changes to this file may cause unexpected behavior in your application.
//     Manual changes to this file will be overwritten if the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

namespace se_liga_mogi.Models
{
    using System;
    using System.Collections.Generic;
    
    public partial class diarias_e_passagens
    {
        public int id_servidor { get; set; }
        public System.DateTime data_inicio { get; set; }
        public System.DateTime data_fim { get; set; }
        public string destino { get; set; }
        public string motivo { get; set; }
        public decimal valor { get; set; }
    
        public virtual servidores servidores { get; set; }
    }
}