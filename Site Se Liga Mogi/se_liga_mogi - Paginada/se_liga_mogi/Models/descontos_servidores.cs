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
    
    public partial class descontos_servidores
    {
        public int id_desconto { get; set; }
        public int rgf { get; set; }
        public string nome_desconto { get; set; }
        public decimal valor_desconto { get; set; }
    
        public virtual servidores servidores { get; set; }
    }
}
